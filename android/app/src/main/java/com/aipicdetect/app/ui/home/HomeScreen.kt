package com.aipicdetect.app.ui.home

import android.content.Intent
import android.graphics.Bitmap
import android.graphics.BitmapFactory
import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.PickVisualMediaRequest
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.aspectRatio
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SnackbarHost
import androidx.compose.material3.SnackbarHostState
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.produceState
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.asImageBitmap
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalResources
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.aipicdetect.app.BuildConfig
import com.aipicdetect.app.R
import com.aipicdetect.app.data.model.AnalyzeResponse
import com.aipicdetect.app.ui.components.AppFooter
import com.aipicdetect.app.ui.components.ErrorBanner
import com.aipicdetect.app.ui.components.FaqSection
import com.aipicdetect.app.ui.components.HowItWorksSection
import com.aipicdetect.app.ui.components.ImageSourceSheet
import com.aipicdetect.app.ui.components.LoadingHint
import com.aipicdetect.app.ui.components.MetadataCard
import com.aipicdetect.app.ui.components.ScoreCard
import com.aipicdetect.app.ui.onboarding.OnboardingSheet
import com.aipicdetect.app.ui.settings.SettingsSheet
import com.aipicdetect.app.ui.theme.Success
import com.aipicdetect.app.util.createCaptureUri
import com.aipicdetect.app.util.findActivity
import com.aipicdetect.app.util.launchInAppReview
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(viewModel: HomeViewModel) {
    val context = LocalContext.current
    val uiState by viewModel.uiState.collectAsState()
    val baseUrl by viewModel.baseUrl.collectAsState()
    val detectorModel by viewModel.detectorModel.collectAsState()
    val detectorReady by viewModel.detectorReady.collectAsState()
    val showOnboarding by viewModel.showOnboarding.collectAsState()
    val snackbarHostState = remember { SnackbarHostState() }
    val activity = remember(context) { context.findActivity() }
    // Read in composition, not inside the event coroutine, so config changes are picked up.
    val resources = LocalResources.current

    var showImageSourceSheet by remember { mutableStateOf(false) }
    var showSettings by remember { mutableStateOf(false) }
    var pendingCaptureUri by remember { mutableStateOf<Uri?>(null) }

    val galleryLauncher = rememberLauncherForActivityResult(ActivityResultContracts.PickVisualMedia()) { uri ->
        uri?.let(viewModel::onImagePicked)
    }
    val cameraLauncher = rememberLauncherForActivityResult(ActivityResultContracts.TakePicture()) { success ->
        if (success) pendingCaptureUri?.let(viewModel::onImagePicked)
    }
    val cameraPermissionLauncher = rememberLauncherForActivityResult(ActivityResultContracts.RequestPermission()) { granted ->
        if (granted) {
            val uri = createCaptureUri(context)
            pendingCaptureUri = uri
            cameraLauncher.launch(uri)
        }
    }

    LaunchedEffect(Unit) {
        viewModel.events.collect { event ->
            when (event) {
                is UiEvent.Snackbar -> snackbarHostState.showSnackbar(resources.getString(event.messageRes))
                is UiEvent.Share -> context.startActivity(Intent.createChooser(event.intent, null))
                UiEvent.RequestReview -> activity?.let { launchInAppReview(it) }
            }
        }
    }

    if (showOnboarding) {
        OnboardingSheet(onFinish = viewModel::onOnboardingFinished)
    }

    if (showImageSourceSheet) {
        ImageSourceSheet(
            onDismiss = { showImageSourceSheet = false },
            onPickFromGallery = {
                showImageSourceSheet = false
                galleryLauncher.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))
            },
            onTakePhoto = {
                showImageSourceSheet = false
                cameraPermissionLauncher.launch(android.Manifest.permission.CAMERA)
            },
        )
    }

    if (showSettings) {
        SettingsSheet(
            currentBaseUrl = baseUrl,
            defaultBaseUrl = BuildConfig.DEFAULT_BASE_URL,
            onDismiss = { showSettings = false },
            onSave = viewModel::updateBaseUrl,
            onResetToDefault = viewModel::resetBaseUrl,
        )
    }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text(stringResource(R.string.app_name)) },
                actions = {
                    StatusPill(ready = detectorReady)
                    IconButton(onClick = { showSettings = true }) {
                        Icon(Icons.Default.Settings, contentDescription = stringResource(R.string.cta_settings))
                    }
                },
            )
        },
        snackbarHost = { SnackbarHost(snackbarHostState) },
    ) { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .verticalScroll(rememberScrollState())
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp),
        ) {
            when (val state = uiState) {
                UiState.Idle -> IdleContent(onChoosePhoto = { showImageSourceSheet = true })
                is UiState.Picked -> PickedContent(
                    uri = state.uri,
                    onAnalyze = viewModel::analyze,
                    onChooseDifferent = { showImageSourceSheet = true },
                )
                is UiState.Analyzing -> {
                    PreviewImage(state.uri)
                    LoadingHint(startedAtMillis = state.startedAtMillis)
                }
                is UiState.Success -> SuccessContent(
                    uri = state.uri,
                    response = state.response,
                    onSave = viewModel::saveCleanCopy,
                    onShare = viewModel::shareCleanCopy,
                    onStartOver = viewModel::startOver,
                )
                is UiState.Failure -> ErrorBanner(error = state.error, onRetry = viewModel::retry)
            }

            HowItWorksSection()
            FaqSection(baseUrl = baseUrl)
            AppFooter(baseUrl = baseUrl, detectorModel = detectorModel)
        }
    }
}

@Composable
private fun IdleContent(onChoosePhoto: () -> Unit) {
    Column(Modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(8.dp)) {
        Text(
            stringResource(R.string.hero_overline).uppercase(),
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
        Column {
            Text(stringResource(R.string.hero_heading_line1), style = MaterialTheme.typography.headlineLarge)
            Text(stringResource(R.string.hero_heading_line2), style = MaterialTheme.typography.headlineLarge)
        }
        Text(
            stringResource(R.string.hero_lead),
            style = MaterialTheme.typography.bodyLarge,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(top = 4.dp, bottom = 8.dp),
        )
        Button(onClick = onChoosePhoto, modifier = Modifier.fillMaxWidth()) {
            Text(stringResource(R.string.cta_pick_image))
        }
    }
}

@Composable
private fun PickedContent(uri: Uri, onAnalyze: () -> Unit, onChooseDifferent: () -> Unit) {
    Column(Modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        PreviewImage(uri)
        Button(onClick = onAnalyze, modifier = Modifier.fillMaxWidth()) {
            Text(stringResource(R.string.cta_analyze))
        }
        OutlinedButton(onClick = onChooseDifferent, modifier = Modifier.fillMaxWidth()) {
            Text(stringResource(R.string.cta_pick_image))
        }
    }
}

@Composable
private fun SuccessContent(
    uri: Uri,
    response: AnalyzeResponse,
    onSave: () -> Unit,
    onShare: () -> Unit,
    onStartOver: () -> Unit,
) {
    Column(Modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(16.dp)) {
        PreviewImage(uri)
        ScoreCard(response.detection)
        MetadataCard(response.metadata)
        response.quota?.let { quota ->
            Text(
                stringResource(R.string.quota_remaining, quota.remaining, quota.limit),
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        Button(onClick = onSave, modifier = Modifier.fillMaxWidth()) {
            Text(stringResource(R.string.cta_save_clean_copy))
        }
        OutlinedButton(onClick = onShare, modifier = Modifier.fillMaxWidth()) {
            Text(stringResource(R.string.cta_share_clean_copy))
        }
        OutlinedButton(onClick = onStartOver, modifier = Modifier.fillMaxWidth()) {
            Text(stringResource(R.string.cta_start_over))
        }
    }
}

@Composable
private fun StatusPill(ready: Boolean) {
    Row(
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(6.dp),
        modifier = Modifier.padding(end = 8.dp),
    ) {
        Box(
            Modifier
                .size(8.dp)
                .background(if (ready) Success else MaterialTheme.colorScheme.onSurfaceVariant, CircleShape),
        )
        Text(
            stringResource(if (ready) R.string.status_detector_ready else R.string.status_detector_loading),
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
    }
}

@Composable
private fun PreviewImage(uri: Uri) {
    val context = LocalContext.current
    val bitmap by produceState<Bitmap?>(initialValue = null, uri) {
        value = withContext(Dispatchers.IO) {
            runCatching {
                context.contentResolver.openInputStream(uri)?.use { BitmapFactory.decodeStream(it) }
            }.getOrNull()
        }
    }
    Box(
        modifier = Modifier
            .fillMaxWidth()
            .aspectRatio(1f)
            .clip(RoundedCornerShape(16.dp))
            .background(MaterialTheme.colorScheme.surfaceVariant),
        contentAlignment = Alignment.Center,
    ) {
        val current = bitmap
        if (current != null) {
            Image(
                bitmap = current.asImageBitmap(),
                contentDescription = stringResource(R.string.cd_picked_image),
                modifier = Modifier.fillMaxSize(),
                contentScale = ContentScale.Crop,
            )
        } else {
            CircularProgressIndicator()
        }
    }
}
