package com.aipicdetect.app

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Surface
import androidx.compose.ui.Modifier
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.lifecycle.viewmodel.initializer
import androidx.lifecycle.viewmodel.viewModelFactory
import com.aipicdetect.app.ui.home.HomeScreen
import com.aipicdetect.app.ui.home.HomeViewModel
import com.aipicdetect.app.ui.theme.AiPicDetectTheme
import com.aipicdetect.app.util.AndroidCleanImageExporter

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()
        setContent {
            AiPicDetectTheme {
                Surface(modifier = Modifier.fillMaxSize()) {
                    val app = application as AiPicDetectApp
                    val viewModel: HomeViewModel = viewModel(
                        factory = viewModelFactory {
                            initializer {
                                HomeViewModel(
                                    AndroidCleanImageExporter(app.applicationContext),
                                    app.settingsRepository,
                                    app.aiPicDetectRepository,
                                    app.engagementRepository,
                                )
                            }
                        },
                    )
                    HomeScreen(viewModel)
                }
            }
        }
    }
}
