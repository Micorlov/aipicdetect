package com.aipicdetect.app.util

import android.content.Context
import android.content.Intent
import android.net.Uri

/** Abstracts "save/share the scrubbed image" so [com.aipicdetect.app.ui.home.HomeViewModel] doesn't need an Android [Context]. */
interface CleanImageExporter {
    fun saveToGallery(bytes: ByteArray, displayName: String, mimeType: String): Uri
    fun shareIntent(bytes: ByteArray, displayName: String, mimeType: String): Intent
}

class AndroidCleanImageExporter(private val context: Context) : CleanImageExporter {
    override fun saveToGallery(bytes: ByteArray, displayName: String, mimeType: String): Uri =
        ImageSaver.saveToGallery(context, bytes, displayName, mimeType)

    override fun shareIntent(bytes: ByteArray, displayName: String, mimeType: String): Intent =
        ImageSaver.shareIntent(context, bytes, displayName, mimeType)
}
