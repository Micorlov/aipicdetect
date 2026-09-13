package com.picai.app.ui.components

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.CameraAlt
import androidx.compose.material.icons.filled.PhotoLibrary
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.ListItem
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import com.picai.app.R

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ImageSourceSheet(
    onDismiss: () -> Unit,
    onPickFromGallery: () -> Unit,
    onTakePhoto: () -> Unit,
) {
    ModalBottomSheet(onDismissRequest = onDismiss) {
        Column(Modifier.fillMaxWidth().padding(bottom = 24.dp), verticalArrangement = Arrangement.spacedBy(4.dp)) {
            ListItem(
                headlineContent = { Text(stringResource(R.string.cta_pick_image)) },
                leadingContent = { Icon(Icons.Default.PhotoLibrary, contentDescription = null) },
                modifier = Modifier.fillMaxWidth().clickable(onClick = onPickFromGallery),
            )
            ListItem(
                headlineContent = { Text(stringResource(R.string.cta_take_photo)) },
                leadingContent = { Icon(Icons.Default.CameraAlt, contentDescription = null) },
                modifier = Modifier.fillMaxWidth().clickable(onClick = onTakePhoto),
            )
        }
    }
}
