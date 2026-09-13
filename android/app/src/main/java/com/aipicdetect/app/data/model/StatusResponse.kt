package com.picai.app.data.model

import kotlinx.serialization.Serializable

/** Mirrors `GET /status` in src/picai/server.py. */
@Serializable
data class StatusResponse(
    val model: String,
    val model_loaded: Boolean,
)
