package com.picai.app.testutil

import android.content.Intent
import android.net.Uri
import com.picai.app.data.PicaiRepository
import com.picai.app.data.SettingsRepository
import com.picai.app.data.model.AnalyzeResponse
import com.picai.app.util.CleanImageExporter
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

class FakePicaiRepository : PicaiRepository {
    var analyzeResult: Result<AnalyzeResponse> = Result.failure(IllegalStateException("analyzeResult not stubbed"))
    var downloadResult: Result<ByteArray> = Result.failure(IllegalStateException("downloadResult not stubbed"))
    var lastAnalyzedUri: Uri? = null

    override suspend fun analyze(uri: Uri): Result<AnalyzeResponse> {
        lastAnalyzedUri = uri
        return analyzeResult
    }

    override suspend fun downloadCleanImage(response: AnalyzeResponse): Result<ByteArray> = downloadResult
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
