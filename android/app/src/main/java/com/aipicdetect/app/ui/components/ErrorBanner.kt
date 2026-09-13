package com.aipicdetect.app.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.aipicdetect.app.R
import com.aipicdetect.app.data.AppError

@Composable
fun ErrorBanner(error: AppError, onRetry: () -> Unit, modifier: Modifier = Modifier) {
    val message = when (error) {
        AppError.NoConnectivity -> stringResource(R.string.error_no_connectivity)
        AppError.Timeout -> stringResource(R.string.error_timeout)
        AppError.TooLarge -> stringResource(R.string.error_too_large)
        AppError.UnsupportedFormat -> stringResource(R.string.error_unsupported_format)
        is AppError.RateLimited -> stringResource(R.string.error_rate_limited, error.detail)
        is AppError.ServerError -> stringResource(R.string.error_unknown, error.detail)
        is AppError.Unknown -> stringResource(R.string.error_unknown, error.detail)
    }
    Card(
        modifier = modifier.fillMaxWidth(),
        colors = CardDefaults.cardColors(containerColor = MaterialTheme.colorScheme.errorContainer),
    ) {
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(12.dp)) {
            Text(
                message,
                style = MaterialTheme.typography.bodyLarge,
                color = MaterialTheme.colorScheme.onErrorContainer,
            )
            Button(onClick = onRetry) { Text(stringResource(R.string.cta_retry)) }
        }
    }
}
