package com.aipicdetect.app.ui.home

import com.aipicdetect.app.data.AppError
import com.aipicdetect.app.data.AppException
import com.aipicdetect.app.data.model.AnalyzeResponse
import com.aipicdetect.app.data.model.Detection
import com.aipicdetect.app.data.model.ImageInfo
import com.aipicdetect.app.data.model.Metadata
import com.aipicdetect.app.data.model.OutputInfo
import com.aipicdetect.app.testutil.FakeCleanImageExporter
import com.aipicdetect.app.testutil.FakeAiPicDetectRepository
import com.aipicdetect.app.testutil.FakeSettingsRepository
import com.aipicdetect.app.testutil.fakeUri
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.test.StandardTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.runTest
import kotlinx.coroutines.test.setMain
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test

@OptIn(ExperimentalCoroutinesApi::class)
class HomeViewModelTest {
    private val dispatcher = StandardTestDispatcher()
    private lateinit var repository: FakeAiPicDetectRepository
    private lateinit var settings: FakeSettingsRepository
    private lateinit var exporter: FakeCleanImageExporter
    private lateinit var viewModel: HomeViewModel

    @Before
    fun setUp() {
        Dispatchers.setMain(dispatcher)
        repository = FakeAiPicDetectRepository()
        settings = FakeSettingsRepository()
        exporter = FakeCleanImageExporter()
        viewModel = HomeViewModel(exporter, settings, repository)
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
}
