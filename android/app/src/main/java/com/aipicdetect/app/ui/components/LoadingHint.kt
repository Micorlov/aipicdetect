package com.aipicdetect.app.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.aipicdetect.app.R
import com.aipicdetect.app.ui.home.COLD_START_HINT_DELAY_MILLIS
import kotlinx.coroutines.delay

@Composable
fun LoadingHint(startedAtMillis: Long, modifier: Modifier = Modifier) {
    var showColdStartHint by remember { mutableStateOf(false) }
    LaunchedEffect(startedAtMillis) {
        val elapsed = System.currentTimeMillis() - startedAtMillis
        val remaining = COLD_START_HINT_DELAY_MILLIS - elapsed
        if (remaining > 0) delay(remaining)
        showColdStartHint = true
    }
    Column(
        modifier = modifier.fillMaxWidth().padding(24.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.spacedBy(12.dp),
    ) {
        CircularProgressIndicator()
        Text(
            stringResource(if (showColdStartHint) R.string.status_cold_start else R.string.status_analyzing),
            style = MaterialTheme.typography.bodyMedium,
        )
    }
}
