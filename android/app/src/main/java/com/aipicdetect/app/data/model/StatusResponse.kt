package com.aipicdetect.app.data.model

import kotlinx.serialization.Serializable

/** Mirrors `GET /status` in src/aipicdetect/server.py. */
@Serializable
data class StatusResponse(
    val model: String,
    val model_loaded: Boolean,
)
