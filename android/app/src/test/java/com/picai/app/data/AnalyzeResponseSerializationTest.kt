package com.picai.app.data

import com.picai.app.data.model.AnalyzeResponse
import com.picai.app.data.model.ErrorResponse
import kotlinx.serialization.json.Json
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

class AnalyzeResponseSerializationTest {
    private val json = Json { ignoreUnknownKeys = true }

    @Test
    fun `decodes a full analyze response matching the server's JSON shape`() {
        val body = """
            {
              "id": "abc123",
              "download_url": "/download/abc123",
              "download_name": "photo.clean.jpg",
              "detection": {
                "ai_likelihood": 0.87,
                "percent": 87,
                "confidence": "High",
                "classification": "AI",
                "model": "haywoodsloan/ai-image-detector-deploy"
              },
              "metadata": {
                "removed": {"EXIF": ["Exif marker"], "IPTC": ["Photoshop 3.0"]},
                "jpeg_app_segments": ["APP1", "APP14"]
              },
              "input": {"bytes": 204800, "width": 1024, "height": 768, "format": "JPEG"},
              "output": {"bytes": 190000, "format": "jpeg", "media_type": "image/jpeg"},
              "quota": {"limit": 10, "remaining": 7, "window_hours": 24}
            }
        """.trimIndent()

        val response = json.decodeFromString<AnalyzeResponse>(body)

        assertEquals("abc123", response.id)
        assertEquals("/download/abc123", response.downloadUrl)
        assertEquals(0.87, response.detection.aiLikelihood, 0.0001)
        assertEquals("AI", response.detection.classification)
        assertTrue(response.metadata.removed.containsKey("EXIF"))
        assertTrue(response.metadata.removed.containsKey("IPTC"))
        assertEquals(false, response.metadata.removed.containsKey("XMP"))
        assertEquals(1024, response.input.width)
        assertEquals(7, response.quota?.remaining)
    }

    @Test
    fun `quota is null when the server has rate limiting disabled`() {
        val body = """
            {
              "id": "abc123",
              "download_url": "/download/abc123",
              "download_name": "photo.clean.jpg",
              "detection": {"ai_likelihood": 0.1, "percent": 10, "confidence": "Low", "classification": "Real", "model": "m"},
              "metadata": {"removed": {}, "jpeg_app_segments": []},
              "input": {"bytes": 100, "width": 10, "height": 10, "format": "PNG"},
              "output": {"bytes": 90, "format": "png", "media_type": "image/png"}
            }
        """.trimIndent()

        val response = json.decodeFromString<AnalyzeResponse>(body)

        assertNull(response.quota)
        assertTrue(response.metadata.removed.isEmpty())
    }

    @Test
    fun `decodes a FastAPI error body's detail field`() {
        val body = """{"detail": "Daily limit reached: 10 images per 24 hours. Try again in about 3 h."}"""

        val error = json.decodeFromString<ErrorResponse>(body)

        assertEquals("Daily limit reached: 10 images per 24 hours. Try again in about 3 h.", error.detail)
    }
}
