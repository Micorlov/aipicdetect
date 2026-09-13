package com.picai.app.ui.components

import android.content.Intent
import android.net.Uri
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.animateContentSize
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.KeyboardArrowDown
import androidx.compose.material.icons.automirrored.filled.KeyboardArrowRight
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.picai.app.R
import com.picai.app.data.AppLinks

private data class FaqEntry(val questionRes: Int, val answerRes: Int)

private val FAQ_ENTRIES = listOf(
    FaqEntry(R.string.faq_q1, R.string.faq_a1),
    FaqEntry(R.string.faq_q2, R.string.faq_a2),
    FaqEntry(R.string.faq_q3, R.string.faq_a3),
    FaqEntry(R.string.faq_q4, R.string.faq_a4),
    FaqEntry(R.string.faq_q5, R.string.faq_a5),
    FaqEntry(R.string.faq_q6, R.string.faq_a6),
    FaqEntry(R.string.faq_q7, R.string.faq_a7),
)

@Composable
fun FaqSection(baseUrl: String, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    Column(modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        Text(
            stringResource(R.string.faq_overline).uppercase(),
            style = MaterialTheme.typography.labelSmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
        Text(
            stringResource(R.string.faq_heading),
            style = MaterialTheme.typography.headlineMedium.copy(fontWeight = MaterialTheme.typography.titleLarge.fontWeight),
        )
        FAQ_ENTRIES.forEach { entry -> FaqRow(entry.questionRes, entry.answerRes) }
        TextButton(onClick = {
            val url = AppLinks.page(baseUrl, "/faq")
            context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))
        }) { Text(stringResource(R.string.faq_more_link)) }
    }
}

@Composable
private fun FaqRow(questionRes: Int, answerRes: Int) {
    var expanded by remember { mutableStateOf(false) }
    Surface(
        color = MaterialTheme.colorScheme.surfaceVariant,
        shape = RoundedCornerShape(6.dp),
        modifier = Modifier
            .fillMaxWidth()
            .animateContentSize()
            .clickable { expanded = !expanded },
    ) {
        Column(Modifier.padding(16.dp)) {
            Row(
                Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.SpaceBetween,
            ) {
                Text(
                    stringResource(questionRes),
                    style = MaterialTheme.typography.titleMedium,
                    modifier = Modifier.weight(1f),
                )
                Icon(
                    if (expanded) Icons.Default.KeyboardArrowDown else Icons.AutoMirrored.Filled.KeyboardArrowRight,
                    contentDescription = stringResource(R.string.cd_faq_expand),
                    tint = MaterialTheme.colorScheme.primary,
                )
            }
            AnimatedVisibility(visible = expanded) {
                Text(
                    stringResource(answerRes),
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(top = 8.dp),
                )
            }
        }
    }
}
