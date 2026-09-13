package com.aipicdetect.app.util

import android.content.Context
import android.net.Uri
import android.provider.OpenableColumns
import okhttp3.MediaType.Companion.toMediaTypeOrNull
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.toRequestBody

data class PickedFile(val bytes: ByteArray, val fileName: String, val mimeType: String)

/** Reads a content [Uri] fully into memory and resolves its display name/MIME type. */
fun Context.readPickedFile(uri: Uri): PickedFile {
    val bytes = contentResolver.openInputStream(uri)?.use { it.readBytes() }
        ?: error("Unable to open $uri")
    val mimeType = contentResolver.getType(uri) ?: "image/jpeg"
    val fileName = queryDisplayName(uri) ?: "upload.${mimeType.substringAfterLast('/', "jpg")}"
    return PickedFile(bytes, fileName, mimeType)
}

private fun Context.queryDisplayName(uri: Uri): String? {
    val projection = arrayOf(OpenableColumns.DISPLAY_NAME)
    return contentResolver.query(uri, projection, null, null, null)?.use { cursor ->
        val nameIndex = cursor.getColumnIndex(OpenableColumns.DISPLAY_NAME)
        if (nameIndex >= 0 && cursor.moveToFirst()) cursor.getString(nameIndex) else null
    }
}

fun PickedFile.toMultipartPart(partName: String = "file"): MultipartBody.Part {
    val requestBody = bytes.toRequestBody(mimeType.toMediaTypeOrNull())
    return MultipartBody.Part.createFormData(partName, fileName, requestBody)
}
