package com.aipicdetect.app.data.model

import kotlinx.serialization.Serializable

/** Shape of FastAPI's default error body: `{"detail": "..."}`. */
@Serializable
data class ErrorResponse(val detail: String? = null)
