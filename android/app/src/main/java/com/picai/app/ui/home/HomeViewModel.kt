package com.picai.app.ui.home

import android.net.Uri
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.picai.app.BuildConfig
import com.picai.app.R
import com.picai.app.data.AppError
import com.picai.app.data.AppException
import com.picai.app.data.PicaiRepository
import com.picai.app.data.SettingsRepository
import com.picai.app.util.CleanImageExporter
import kotlinx.coroutines.flow.MutableSharedFlow
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asSharedFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

/** How long [UiState.Analyzing] waits before the UI should show the cold-start hint. */
const val COLD_START_HINT_DELAY_MILLIS = 8_000L

class HomeViewModel(
    private val exporter: CleanImageExporter,
    private val settingsRepository: SettingsRepository,
    private val repository: PicaiRepository,
) : ViewModel() {

    private val _uiState = MutableStateFlow<UiState>(UiState.Idle)
    val uiState: StateFlow<UiState> = _uiState.asStateFlow()

    private val _events = MutableSharedFlow<UiEvent>()
    val events = _events.asSharedFlow()

    val baseUrl: StateFlow<String> =
        settingsRepository.baseUrl.stateIn(viewModelScope, SharingStarted.Eagerly, BuildConfig.DEFAULT_BASE_URL)

    fun onImagePicked(uri: Uri) {
        _uiState.value = UiState.Picked(uri)
    }

    fun analyze() {
        val uri = (_uiState.value as? UiState.Picked)?.uri ?: return
        _uiState.value = UiState.Analyzing(uri, System.currentTimeMillis())
        viewModelScope.launch {
            repository.analyze(uri)
                .onSuccess { response -> _uiState.value = UiState.Success(uri, response) }
                .onFailure { error -> _uiState.value = UiState.Failure(uri, error.toAppError()) }
        }
    }

    fun startOver() {
        _uiState.value = UiState.Idle
    }

    fun retry() {
        val uri = (_uiState.value as? UiState.Failure)?.uri
        _uiState.value = if (uri != null) UiState.Picked(uri) else UiState.Idle
    }

    fun saveCleanCopy() {
        val state = _uiState.value as? UiState.Success ?: return
        viewModelScope.launch {
            repository.downloadCleanImage(state.response)
                .onSuccess { bytes ->
                    runCatching {
                        exporter.saveToGallery(bytes, state.response.downloadName, state.response.output.mediaType)
                    }.onSuccess { _events.emit(UiEvent.Snackbar(R.string.status_saved)) }
                        .onFailure { _events.emit(UiEvent.Snackbar(R.string.error_save_failed)) }
                }
                .onFailure { _events.emit(UiEvent.Snackbar(R.string.error_save_failed)) }
        }
    }

    fun shareCleanCopy() {
        val state = _uiState.value as? UiState.Success ?: return
        viewModelScope.launch {
            repository.downloadCleanImage(state.response)
                .onSuccess { bytes ->
                    val intent = exporter.shareIntent(bytes, state.response.downloadName, state.response.output.mediaType)
                    _events.emit(UiEvent.Share(intent))
                }
                .onFailure { _events.emit(UiEvent.Snackbar(R.string.error_share_failed)) }
        }
    }

    fun updateBaseUrl(url: String) {
        viewModelScope.launch { settingsRepository.setBaseUrl(url) }
    }

    fun resetBaseUrl() {
        viewModelScope.launch { settingsRepository.resetToDefault() }
    }
}

private fun Throwable.toAppError(): AppError = (this as? AppException)?.error ?: AppError.Unknown(message ?: "unknown error")
