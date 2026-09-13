package com.aipicdetect.app.data

import kotlinx.coroutines.test.runTest
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.MultipartBody
import okhttp3.RequestBody.Companion.toRequestBody
import okhttp3.mockwebserver.MockResponse
import okhttp3.mockwebserver.MockWebServer
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test

/** Exercises the real Retrofit/OkHttp/kotlinx.serialization wiring against a local MockWebServer. */
class AiPicDetectApiServiceTest {
    private lateinit var server: MockWebServer

    @Before
    fun setUp() {
        server = MockWebServer()
        server.start()
    }

    @After
    fun tearDown() {
        server.shutdown()
    }

    private fun fakeImagePart(): MultipartBody.Part {
        val body = "fake-image-bytes".toRequestBody("image/jpeg".toMediaType())
        return MultipartBody.Part.createFormData("file", "test.jpg", body)
    }

    @Test
    fun `analyze parses a successful response into AnalyzeResponse`() = runTest {
        val json = """
            {
              "id": "abc123",
              "download_url": "/download/abc123",
              "download_name": "photo.clean.jpg",
              "detection": {"ai_likelihood": 0.87, "percent": 87, "confidence": "High", "classification": "AI", "model": "m"},
              "metadata": {"removed": {"EXIF": ["Exif marker"]}, "jpeg_app_segments": []},
              "input": {"bytes": 100, "width": 10, "height": 10, "format": "JPEG"},
              "output": {"bytes": 90, "format": "jpeg", "media_type": "image/jpeg"},
              "quota": {"limit": 10, "remaining": 9, "window_hours": 24}
            }
        """.trimIndent()
        server.enqueue(MockResponse().setResponseCode(200).setBody(json).setHeader("Content-Type", "application/json"))

        val api = NetworkModule.apiServiceFor(server.url("/").toString())
        val response = api.analyze(fakeImagePart())

        assertTrue(response.isSuccessful)
        assertEquals("abc123", response.body()?.id)
        assertEquals(9, response.body()?.quota?.remaining)
    }

    @Test
    fun `analyze surfaces a 429 as a non-successful response with the detail body intact`() = runTest {
        server.enqueue(
            MockResponse()
                .setResponseCode(429)
                .setBody("""{"detail": "Daily limit reached: 10 images per 24 hours. Try again in about 3 h."}""")
                .setHeader("Content-Type", "application/json"),
        )

        val api = NetworkModule.apiServiceFor(server.url("/").toString())
        val response = api.analyze(fakeImagePart())

        assertFalse(response.isSuccessful)
        assertEquals(429, response.code())
        val mapped = ErrorMapper.fromResponse(response)
        assertTrue(mapped is AppError.RateLimited)
    }
}
