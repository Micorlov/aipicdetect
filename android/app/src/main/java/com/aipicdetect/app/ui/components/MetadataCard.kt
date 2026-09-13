package com.aipicdetect.app.ui.components

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.aipicdetect.app.R
import com.aipicdetect.app.data.model.Metadata

private val STANDARD_METADATA_BLOCKS = listOf("EXIF", "XMP", "IPTC", "C2PA", "ICC")

@Composable
fun MetadataCard(metadata: Metadata, modifier: Modifier = Modifier) {
    Card(modifier = modifier.fillMaxWidth()) {
        Column(Modifier.padding(16.dp), verticalArrangement = Arrangement.spacedBy(10.dp)) {
            Text(stringResource(R.string.section_metadata), style = MaterialTheme.typography.titleMedium)
            STANDARD_METADATA_BLOCKS.forEach { block ->
                MetadataBlockRow(name = block, signatures = metadata.removed[block])
            }
            val segmentsText = if (metadata.jpegAppSegments.isEmpty()) {
                stringResource(R.string.jpeg_segments_empty)
            } else {
                stringResource(R.string.jpeg_segments_label, metadata.jpegAppSegments.joinToString(", "))
            }
            Text(segmentsText, style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}

@Composable
private fun MetadataBlockRow(name: String, signatures: List<String>?) {
    val found = !signatures.isNullOrEmpty()
    Column {
        Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.SpaceBetween) {
            Text(name, style = MaterialTheme.typography.bodyLarge)
            Text(
                stringResource(if (found) R.string.metadata_present else R.string.metadata_not_present),
                style = MaterialTheme.typography.bodyMedium,
                color = if (found) MaterialTheme.colorScheme.error else MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        if (found) {
            val joined = signatures.orEmpty().joinToString(separator = ", ") { it.trim() }
            Text(joined, style = MaterialTheme.typography.bodyMedium, color = MaterialTheme.colorScheme.onSurfaceVariant)
        }
    }
}
