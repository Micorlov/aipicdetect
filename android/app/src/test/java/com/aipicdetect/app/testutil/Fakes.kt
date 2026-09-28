package com.aipicdetect.app.testutil

import android.content.Intent
import android.net.Uri
import com.aipicdetect.app.data.AiPicDetectRepository
import com.aipicdetect.app.data.EngagementRepository
import com.aipicdetect.app.data.REVIEW_PROMPT_THRESHOLD
import com.aipicdetect.app.data.SettingsRepository
import com.aipicdetect.app.data.model.AnalyzeResponse
import com.aipicdetect.app.data.model.StatusResponse
import com.aipicdetect.app.util.CleanImageExporter
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.MutableStateFlow
import org.mockito.Mockito

/**
 * The JVM unit-test `android.jar` stub has no real logic behind `android.net.Uri`/`Intent`, so
 * a plain `Uri.EMPTY` or `Uri.parse(...)` NPEs. Mockito instances sidestep that — they never
 * touch the stub method bodies.
 */
fun fakeUri(): Uri = Mockito.mock(Uri::class.java)

private fun fakeIntent(): Intent = Mockito.mock(Intent::class.java)

class FakeAiPicDetectRepository : AiPicDetectRepository {
    var analyzeResult: Result<AnalyzeResponse> = Result.failure(IllegalStateException("analyzeResult not stubbed"))
    var downloadResult: Result<ByteArray> = Result.failure(IllegalStateException("downloadResult not stubbed"))
    var detectorStatusResult: Result<StatusResponse> = Result.success(StatusResponse("test-model", true))
    var lastAnalyzedUri: Uri? = null

    override suspend fun analyze(uri: Uri): Result<AnalyzeResponse> {
        lastAnalyzedUri = uri
        return analyzeResult
    }

    override suspend fun downloadCleanImage(response: AnalyzeResponse): Result<ByteArray> = downloadResult

    override suspend fun fetchDetectorStatus(): Result<StatusResponse> = detectorStatusResult
}

class FakeSettingsRepository(private val initial: String = "https://example.test") : SettingsRepository {
    private val state = MutableStateFlow(initial)
    override val baseUrl: Flow<String> = state

    override suspend fun setBaseUrl(url: String) {
        state.value = url
    }

    override suspend fun resetToDefault() {
        state.value = initial
    }
}

class FakeCleanImageExporter : CleanImageExporter {
    var savedBytes: ByteArray? = null
    var sharedBytes: ByteArray? = null
    var shouldFailSave: Boolean = false

    override fun saveToGallery(bytes: ByteArray, displayName: String, mimeType: String): Uri {
        if (shouldFailSave) error("save failed")
        savedBytes = bytes
        return fakeUri()
    }

    override fun shareIntent(bytes: ByteArray, displayName: String, mimeType: String): Intent {
        sharedBytes = bytes
        return fakeIntent()
    }
}

/**
 * In-memory [EngagementRepository]. Defaults to onboarding already seen so tests that don't
 * care about first-run behaviour aren't implicitly exercising the walkthrough.
 */
class FakeEngagementRepository(hasSeenOnboarding: Boolean = true) : EngagementRepository {
    private val seen = MutableStateFlow(hasSeenOnboarding)

    var successfulAnalyses: Int = 0
        private set
    var reviewOffered: Boolean = false
        private set

    override val hasSeenOnboarding: Flow<Boolean> = seen

    override suspend fun markOnboardingSeen() {
        seen.value = true
    }

    override suspend fun recordSuccessfulAnalysis() {
        successfulAnalyses += 1
    }

    override suspend fun shouldOfferReview(): Boolean =
        !reviewOffered && successfulAnalyses >= REVIEW_PROMPT_THRESHOLD

    override suspend fun markReviewOffered() {
        reviewOffered = true
    }
}
