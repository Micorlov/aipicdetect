package com.picai.app.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.LinearProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.picai.app.R
import com.picai.app.data.model.Detection
import com.picai.app.ui.theme.Danger
import com.picai.app.ui.theme.Success
import com.picai.app.ui.theme.Warn

@Composable
fun ScoreCard(detection: Detection, modifier: Modifier = Modifier) {
    val label = when (detection.classification) {
        "AI" -> stringResource(R.string.score_label_ai)
        "Real" -> stringResource(R.string.score_label_real)
        else -> stringResource(R.string.score_label_uncertain)
    }
    val tone = when (detection.classification) {
        "AI" -> Danger
        "Real" -> Success
        else -> Warn
    }

    Card(modifier = modifier.fillMaxWidth(), colors = CardDefaults.cardColors()) {
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(8.dp)) {
            Text(stringResource(R.string.section_detection), style = MaterialTheme.typography.titleMedium)
            Text(
                stringResource(R.string.score_percent_line, label, detection.percent),
                style = MaterialTheme.typography.headlineMedium,
                color = tone,
            )
            LinearProgressIndicator(
                progress = { detection.aiLikelihood.toFloat().coerceIn(0f, 1f) },
                modifier = Modifier.fillMaxWidth(),
                color = tone,
                trackColor = tone.copy(alpha = 0.14f),
            )
            Text(
                stringResource(R.string.score_confidence_line, detection.confidence, detection.model),
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
    }
}
