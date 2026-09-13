package com.picai.app.data

import okhttp3.MediaType.Companion.toMediaType
import okhttp3.ResponseBody.Companion.toResponseBody
import org.junit.Assert.assertEquals
import org.junit.Assert.assertTrue
import org.junit.Test
import retrofit2.Response

class ErrorMapperTest {

    private fun errorResponse(code: Int, body: String?): Response<Any> =
        Response.error(code, (body ?: "").toResponseBody("application/json".toMediaType()))

    @Test
    fun `413 maps to TooLarge`() {
        val error = ErrorMapper.fromResponse(errorResponse(413, """{"detail": "upload exceeds 50 MB"}"""))
        assertTrue(error is AppError.TooLarge)
    }

    @Test
    fun `415 maps to UnsupportedFormat`() {
        val error = ErrorMapper.fromResponse(errorResponse(415, """{"detail": "unsupported image"}"""))
        assertTrue(error is AppError.UnsupportedFormat)
    }

    @Test
    fun `429 maps to RateLimited carrying the server's detail message`() {
        val detail = "Daily limit reached: 10 images per 24 hours. Try again in about 3 h."
        val error = ErrorMapper.fromResponse(errorResponse(429, """{"detail": "$detail"}"""))
        assertEquals(AppError.RateLimited(detail), error)
    }

    @Test
    fun `unrecognized status codes map to ServerError with the parsed detail`() {
        val error = ErrorMapper.fromResponse(errorResponse(500, """{"detail": "internal error"}"""))
        assertEquals(AppError.ServerError(500, "internal error"), error)
    }

    @Test
    fun `falls back to a generic message when the error body isn't valid JSON`() {
        val error = ErrorMapper.fromResponse(errorResponse(502, "Bad Gateway"))
        assertEquals(AppError.ServerError(502, "Bad Gateway"), error)
    }

    @Test
    fun `falls back to HTTP code when the error body is empty`() {
        val error = ErrorMapper.fromResponse(errorResponse(500, null))
        assertEquals(AppError.ServerError(500, "HTTP 500"), error)
    }
}
