package com.picai.app.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.picai.app.R

private data class Step(val number: String, val titleRes: Int, val bodyRes: Int)

private val STEPS = listOf(
    Step("1", R.string.how_step1_title, R.string.how_step1_body),
    Step("2", R.string.how_step2_title, R.string.how_step2_body),
    Step("3", R.string.how_step3_title, R.string.how_step3_body),
)

@Composable
fun HowItWorksSection(modifier: Modifier = Modifier) {
    Column(modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(
            stringResource(R.string.how_overline).uppercase(),
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
        Text(
            stringResource(R.string.how_heading),
            style = MaterialTheme.typography.headlineMedium.copy(fontWeight = MaterialTheme.typography.titleLarge.fontWeight),
        )
        STEPS.forEach { step ->
            Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(12.dp)) {
                Surface(shape = CircleShape, color = MaterialTheme.colorScheme.primary, modifier = Modifier.size(28.dp)) {
                    Box(contentAlignment = Alignment.Center) {
                        Text(
                            step.number,
                            style = MaterialTheme.typography.labelLarge,
                            color = MaterialTheme.colorScheme.onPrimary,
                        )
                    }
                }
                Column(verticalArrangement = Arrangement.spacedBy(2.dp)) {
                    Text(stringResource(step.titleRes), style = MaterialTheme.typography.titleMedium)
                    Text(
                        stringResource(step.bodyRes),
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }
        }
    }
}
