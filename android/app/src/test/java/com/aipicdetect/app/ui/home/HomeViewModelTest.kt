package com.aipicdetect.app.ui.home

import com.aipicdetect.app.data.AppError
import com.aipicdetect.app.data.AppException
import com.aipicdetect.app.data.model.AnalyzeResponse
import com.aipicdetect.app.data.model.Detection
import com.aipicdetect.app.data.model.ImageInfo
import com.aipicdetect.app.data.model.Metadata
import com.aipicdetect.app.data.model.OutputInfo
import com.aipicdetect.app.data.REVIEW_PROMPT_THRESHOLD
import com.aipicdetect.app.testutil.FakeCleanImageExporter
import com.aipicdetect.app.testutil.FakeEngagementRepository
import com.aipicdetect.app.testutil.FakeAiPicDetectRepository
import com.aipicdetect.app.testutil.FakeSettingsRepository
import com.aipicdetect.app.testutil.fakeUri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.TestScope
import kotlinx.coroutines.test.UnconfinedTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class HomeViewModelTest {
    private val dispatcher = StandardTestDispatcher()
    private lateinit var repository: FakeAiPicDetectRepository
    private lateinit var settings: FakeSettingsRepository
    private lateinit var exporter: FakeCleanImageExporter
    private lateinit var engagement: FakeEngagementRepository
    private lateinit var viewModel: HomeViewModel

    @Before
    fun setUp() {
        Dispatchers.setMain(dispatcher)
        repository = FakeAiPicDetectRepository()
        settings = FakeSettingsRepository()
        exporter = FakeCleanImageExporter()
        engagement = FakeEngagementRepository()
        viewModel = HomeViewModel(exporter, settings, repository, engagement)
    }

    @After
    fun tearDown() {
        Dispatchers.resetMain()
    }

    private fun sampleResponse() = AnalyzeResponse(
        id = "abc",
        downloadUrl = "/download/abc",
        downloadName = "photo.clean.jpg",
        detection = Detection(0.9, 90, "High", "AI", "model"),
        metadata = Metadata(mapOf("EXIF" to listOf("Exif marker")), emptyList()),
        input = ImageInfo(100, 10, 10, "JPEG"),
        output = OutputInfo(90, "jpeg", "image/jpeg"),
        quota = null,
    )

    @Test
    fun `starts in Idle state`() = runTest {
        assertEquals(UiState.Idle, viewModel.uiState.value)
    }

    @Test
    fun `picking an image moves to Picked`() = runTest {
        val uri = fakeUri()
        viewModel.onImagePicked(uri)
        assertEquals(UiState.Picked(uri), viewModel.uiState.value)
    }

    @Test
    fun `analyze on success moves to Success with the response`() = runTest {
        val response = sampleResponse()
        repository.analyzeResult = Result.success(response)
        viewModel.onImagePicked(fakeUri())

        viewModel.analyze()
        dispatcher.scheduler.advanceUntilIdle()

        val state = viewModel.uiState.value
        assertTrue(state is UiState.Success)
        assertEquals(response, (state as UiState.Success).response)
    }

    @Test
    fun `analyze on failure moves to Failure carrying the mapped error`() = runTest {
        repository.analyzeResult = Result.failure(AppException(AppError.TooLarge))
        viewModel.onImagePicked(fakeUri())

        viewModel.analyze()
        dispatcher.scheduler.advanceUntilIdle()

        val state = viewModel.uiState.value
        assertTrue(state is UiState.Failure)
        assertEquals(AppError.TooLarge, (state as UiState.Failure).error)
    }

    @Test
    fun `retry after failure returns to Picked with the same uri`() = runTest {
        val uri = fakeUri()
        repository.analyzeResult = Result.failure(AppException(AppError.Timeout))
        viewModel.onImagePicked(uri)
        viewModel.analyze()
        dispatcher.scheduler.advanceUntilIdle()

        viewModel.retry()

        assertEquals(UiState.Picked(uri), viewModel.uiState.value)
    }

    @Test
    fun `startOver resets to Idle from Success`() = runTest {
        repository.analyzeResult = Result.success(sampleResponse())
        viewModel.onImagePicked(fakeUri())
        viewModel.analyze()
        dispatcher.scheduler.advanceUntilIdle()

        viewModel.startOver()

        assertEquals(UiState.Idle, viewModel.uiState.value)
    }

    @Test
    fun `saveCleanCopy downloads the clean image and hands the bytes to the exporter`() = runTest {
        repository.analyzeResult = Result.success(sampleResponse())
        repository.downloadResult = Result.success(byteArrayOf(1, 2, 3))
        viewModel.onImagePicked(fakeUri())
        viewModel.analyze()
        dispatcher.scheduler.advanceUntilIdle()

        viewModel.saveCleanCopy()
        dispatcher.scheduler.advanceUntilIdle()

        assertTrue(exporter.savedBytes!!.contentEquals(byteArrayOf(1, 2, 3)))
    }

    /**
     * Collects [HomeViewModel.events] eagerly. An unconfined dispatcher is required here:
     * the events flow has no replay, so a collector that only resumes on scheduler pumps
     * can miss an emission entirely.
     */
    private fun TestScope.recordEvents(): List<UiEvent> {
        val received = mutableListOf<UiEvent>()
        backgroundScope.launch(UnconfinedTestDispatcher(testScheduler)) {
            viewModel.events.collect { received += it }
        }
        return received
    }

    private fun analyzeSuccessfully(times: Int) {
        repository.analyzeResult = Result.success(sampleResponse())
        repeat(times) {
            viewModel.onImagePicked(fakeUri())
            viewModel.analyze()
            dispatcher.scheduler.advanceUntilIdle()
        }
    }

    @Test
    fun `showOnboarding is false once the walkthrough has been seen`() = runTest {
        dispatcher.scheduler.advanceUntilIdle()
        assertFalse(viewModel.showOnboarding.value)
    }

    @Test
    fun `showOnboarding is true on a first run`() = runTest {
        val firstRun = FakeEngagementRepository(hasSeenOnboarding = false)
        val freshViewModel = HomeViewModel(exporter, settings, repository, firstRun)
        dispatcher.scheduler.advanceUntilIdle()

        assertTrue(freshViewModel.showOnboarding.value)
    }

    @Test
    fun `finishing onboarding hides it for good`() = runTest {
        val firstRun = FakeEngagementRepository(hasSeenOnboarding = false)
        val freshViewModel = HomeViewModel(exporter, settings, repository, firstRun)
        dispatcher.scheduler.advanceUntilIdle()

        freshViewModel.onOnboardingFinished()
        dispatcher.scheduler.advanceUntilIdle()

        assertFalse(freshViewModel.showOnboarding.value)
    }

    @Test
    fun `no review is requested before the threshold is reached`() = runTest {
        val events = recordEvents()

        analyzeSuccessfully(REVIEW_PROMPT_THRESHOLD - 1)

        assertFalse(events.contains(UiEvent.RequestReview))
        assertFalse(engagement.reviewOffered)
    }

    @Test
    fun `a review is requested once the threshold is reached`() = runTest {
        val events = recordEvents()

        analyzeSuccessfully(REVIEW_PROMPT_THRESHOLD)

        assertEquals(1, events.count { it == UiEvent.RequestReview })
        assertTrue(engagement.reviewOffered)
    }

    @Test
    fun `the review prompt is never offered twice`() = runTest {
        val events = recordEvents()

        analyzeSuccessfully(REVIEW_PROMPT_THRESHOLD + 3)

        assertEquals(1, events.count { it == UiEvent.RequestReview })
    }

    @Test
    fun `a failed analysis does not count towards the review prompt`() = runTest {
        repository.analyzeResult = Result.failure(AppException(AppError.Timeout))
        repeat(REVIEW_PROMPT_THRESHOLD) {
            viewModel.onImagePicked(fakeUri())
            viewModel.analyze()
            dispatcher.scheduler.advanceUntilIdle()
        }

        assertEquals(0, engagement.successfulAnalyses)
        assertFalse(engagement.reviewOffered)
    }
}
