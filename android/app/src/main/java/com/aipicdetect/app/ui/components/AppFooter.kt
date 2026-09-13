package com.aipicdetect.app.ui.components

import android.content.Intent
import android.net.Uri
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.dp
import com.aipicdetect.app.R
import com.aipicdetect.app.data.AppLinks

private data class FooterLink(val labelRes: Int, val path: String)

private val DOC_LINKS = listOf(
    FooterLink(R.string.footer_link_remove_metadata, "/remove-image-metadata"),
    FooterLink(R.string.footer_link_c2pa, "/c2pa"),
    FooterLink(R.string.footer_link_faq, "/faq"),
    FooterLink(R.string.footer_link_privacy, "/privacy"),
    FooterLink(R.string.footer_link_selfhost, "/self-host"),
    FooterLink(R.string.footer_link_about, "/about"),
)

@Composable
fun AppFooter(baseUrl: String, detectorModel: String?, modifier: Modifier = Modifier) {
    val context = LocalContext.current
    fun open(url: String) = context.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))

    Column(modifier.fillMaxWidth(), verticalArrangement = Arrangement.spacedBy(12.dp)) {
        HorizontalDivider()
        Text(
            stringResource(R.string.footer_tagline),
            style = MaterialTheme.typography.bodyMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
        detectorModel?.let { model ->
            Text(
                stringResource(R.string.footer_detector, model),
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        FlowRow(horizontalArrangement = Arrangement.spacedBy(16.dp)) {
            (DOC_LINKS.map { it.labelRes to AppLinks.page(baseUrl, it.path) } + (R.string.footer_link_github to AppLinks.REPO_URL))
                .forEach { (labelRes, url) ->
                    Text(
                        stringResource(labelRes),
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.primary,
                        textDecoration = TextDecoration.Underline,
                        modifier = Modifier.clickable { open(url) },
                    )
                }
        }
    }
}
