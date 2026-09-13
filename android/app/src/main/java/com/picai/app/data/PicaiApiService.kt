package com.picai.app.data

import com.picai.app.data.model.AnalyzeResponse
import com.picai.app.data.model.StatusResponse
import okhttp3.MultipartBody
import okhttp3.ResponseBody
import retrofit2.Response
import retrofit2.http.GET
import retrofit2.http.Multipart
import retrofit2.http.POST
import retrofit2.http.Part
import retrofit2.http.Url

/**
 * Mirrors the endpoints the app needs from `src/picai/server.py`. Errors
 * are surfaced as HTTP responses (not exceptions) so [PicaiRepository] can
 * read the status code and JSON `detail` body for 413/415/429 and map them
 * to [AppError] precisely.
 */
interface PicaiApiService {
    @Multipart
    @POST("analyze")
    suspend fun analyze(
        @Part file: MultipartBody.Part,
    ): Response<AnalyzeResponse>

    @GET
    suspend fun download(@Url url: String): Response<ResponseBody>

    @GET("status")
    suspend fun status(): Response<StatusResponse>
}
