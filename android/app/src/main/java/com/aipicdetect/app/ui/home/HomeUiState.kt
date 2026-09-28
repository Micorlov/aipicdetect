package com.aipicdetect.app.ui.home

import android.content.Intent
import android.net.Uri
import androidx.annotation.StringRes
import com.aipicdetect.app.data.AppError
import com.aipicdetect.app.data.model.AnalyzeResponse

sealed interface UiState {
    data object Idle : UiState
    data class Picked(val uri: Uri) : UiState
    data class Analyzing(val uri: Uri, val startedAtMillis: Long) : UiState
    data class Success(val uri: Uri, val response: AnalyzeResponse) : UiState
    data class Failure(val uri: Uri?, val error: AppError) : UiState
}

sealed interface UiEvent {
    data class Snackbar(@StringRes val messageRes: Int) : UiEvent
    data class Share(val intent: Intent) : UiEvent

    /** Ask Play for its in-app review card; the screen owns the Activity it needs. */
    data object RequestReview : UiEvent
}
