package com.aipicdetect.app.data

/**
 * Every failure the UI needs to distinguish. The fixed cases render a canned
 * string resource; the server-driven cases carry AiPicDetect's own message through
 * verbatim since it already explains limits/retry windows in plain English.
 */
sealed interface AppError {
    data object NoConnectivity : AppError
    data object Timeout : AppError
    data object TooLarge : AppError
    data object UnsupportedFormat : AppError
    data class RateLimited(val detail: String) : AppError
    data class ServerError(val code: Int, val detail: String) : AppError
    data class Unknown(val detail: String) : AppError
}
