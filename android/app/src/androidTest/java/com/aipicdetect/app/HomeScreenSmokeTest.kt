package com.aipicdetect.app

import android.content.Intent
import android.net.Uri
import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithText
import com.aipicdetect.app.data.AiPicDetectRepository
import com.aipicdetect.app.data.SettingsRepository
import com.aipicdetect.app.data.model.AnalyzeResponse
import com.aipicdetect.app.ui.home.HomeScreen
import com.aipicdetect.app.ui.home.HomeViewModel
import com.aipicdetect.app.ui.theme.AiPicDetectTheme
import com.aipicdetect.app.util.CleanImageExporter
import kotlinx.coroutines.flow.MutableStateFlow
import org.junit.Rule
import org.junit.Test

/** Minimal instrumented smoke test: the idle screen renders its main call to action. */
class HomeScreenSmokeTest {
    @get:Rule
    val composeRule = createComposeRule()

    private class NoopRepository : AiPicDetectRepository {
        override suspend fun analyze(uri: Uri): Result<AnalyzeResponse> =
            Result.failure(IllegalStateException("not used in this test"))

        override suspend fun downloadCleanImage(response: AnalyzeResponse): Result<ByteArray> =
            Result.failure(IllegalStateException("not used in this test"))
    }

    private class StaticSettingsRepository : SettingsRepository {
        override val baseUrl = MutableStateFlow("https://example.test")
        override suspend fun setBaseUrl(url: String) = Unit
        override suspend fun resetToDefault() = Unit
    }

    private class NoopExporter : CleanImageExporter {
        override fun saveToGallery(bytes: ByteArray, displayName: String, mimeType: String): Uri = Uri.EMPTY
        override fun shareIntent(bytes: ByteArray, displayName: String, mimeType: String): Intent = Intent()
    }

    @Test
    fun idleState_showsChoosePhotoButton() {
        val viewModel = HomeViewModel(NoopExporter(), StaticSettingsRepository(), NoopRepository())
        composeRule.setContent {
            AiPicDetectTheme { HomeScreen(viewModel) }
        }
        composeRule.onNodeWithText("Choose a photo").assertIsDisplayed()
    }
}
