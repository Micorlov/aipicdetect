package com.aipicdetect.app.data

import com.aipicdetect.app.data.model.ErrorResponse
import kotlinx.serialization.json.Json
import retrofit2.Response

/** Maps a non-2xx Retrofit [Response] to an [AppError], reading AiPicDetect's `{"detail": "..."}` body when present. */
object ErrorMapper {
    private val json = Json { ignoreUnknownKeys = true }

    fun fromResponse(response: Response<*>): AppError {
        val code = response.code()
        val detail = parseDetail(response) ?: "HTTP $code"
        return when (code) {
            413 -> AppError.TooLarge
            415 -> AppError.UnsupportedFormat
            429 -> AppError.RateLimited(detail)
            else -> AppError.ServerError(code, detail)
        }
    }

    private fun parseDetail(response: Response<*>): String? {
        val raw = response.errorBody()?.string()?.takeIf { it.isNotBlank() } ?: return null
        return runCatching { json.decodeFromString<ErrorResponse>(raw).detail }
            .getOrNull()
            ?: raw
    }
}
