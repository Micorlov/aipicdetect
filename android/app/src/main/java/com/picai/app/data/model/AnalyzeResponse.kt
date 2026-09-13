package com.picai.app.data.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
data class AnalyzeResponse(
    val id: String,
    @SerialName("download_url") val downloadUrl: String,
    @SerialName("download_name") val downloadName: String,
    val detection: Detection,
    val metadata: Metadata,
    val input: ImageInfo,
    val output: OutputInfo,
    val quota: Quota? = null,
)

@Serializable
data class Detection(
    @SerialName("ai_likelihood") val aiLikelihood: Double,
    val percent: Int,
    val confidence: String,
    val classification: String,
    val model: String,
)

/**
 * `removed` mirrors `find_metadata()` in `src/picai/inspect.py`: `{category: [matched signatures]}`,
 * with a category key present only when at least one signature was found in it.
 */
@Serializable
data class Metadata(
    val removed: Map<String, List<String>>,
    @SerialName("jpeg_app_segments") val jpegAppSegments: List<String>,
)

@Serializable
data class ImageInfo(
    val bytes: Long,
    val width: Int,
    val height: Int,
    val format: String? = null,
)

@Serializable
data class OutputInfo(
    val bytes: Long,
    val format: String,
    @SerialName("media_type") val mediaType: String,
)

@Serializable
data class Quota(
    val limit: Int,
    val remaining: Int,
    @SerialName("window_hours") val windowHours: Int,
)
