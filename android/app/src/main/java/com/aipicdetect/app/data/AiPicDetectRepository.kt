package com.aipicdetect.app.data

import android.content.Context
import android.net.Uri
import com.aipicdetect.app.data.model.AnalyzeResponse
import com.aipicdetect.app.data.model.StatusResponse
import com.aipicdetect.app.util.readPickedFile
import com.aipicdetect.app.util.toMultipartPart
import java.io.IOException
import java.net.SocketTimeoutException
import kotlinx.coroutines.flow.first
import retrofit2.Response

/** Mirrors `MAX_UPLOAD_MB` in `src/aipicdetect/limits.py` so we can reject oversized files before a network call. */
private const val MAX_UPLOAD_BYTES = 50L * 1024 * 1024

interface AiPicDetectRepository {
    suspend fun analyze(uri: Uri): Result<AnalyzeResponse>
    suspend fun downloadCleanImage(response: AnalyzeResponse): Result<ByteArray>
    suspend fun fetchDetectorStatus(): Result<StatusResponse>
}

class AiPicDetectRepositoryImpl(
    private val context: Context,
    private val settingsRepository: SettingsRepository,
) : AiPicDetectRepository {

    override suspend fun analyze(uri: Uri): Result<AnalyzeResponse> = runCatching {
        val picked = context.readPickedFile(uri)
        if (picked.bytes.size > MAX_UPLOAD_BYTES) {
            throw AppException(AppError.TooLarge)
        }
        val api = NetworkModule.apiServiceFor(settingsRepository.baseUrl.first())
        val response = safeCall { api.analyze(picked.toMultipartPart()) }
        response.body() ?: throw AppException(ErrorMapper.fromResponse(response))
    }

    override suspend fun downloadCleanImage(response: AnalyzeResponse): Result<ByteArray> = runCatching {
        val api = NetworkModule.apiServiceFor(settingsRepository.baseUrl.first())
        val httpResponse = safeCall { api.download(response.downloadUrl) }
        httpResponse.body()?.bytes() ?: throw AppException(ErrorMapper.fromResponse(httpResponse))
    }

    override suspend fun fetchDetectorStatus(): Result<StatusResponse> = runCatching {
        val api = NetworkModule.apiServiceFor(settingsRepository.baseUrl.first())
        val response = safeCall { api.status() }
        response.body() ?: throw AppException(ErrorMapper.fromResponse(response))
    }

    private suspend fun <T> safeCall(block: suspend () -> Response<T>): Response<T> = try {
        block()
    } catch (e: SocketTimeoutException) {
        throw AppException(AppError.Timeout, e)
    } catch (e: IOException) {
        throw AppException(AppError.NoConnectivity, e)
    }
}

/** Wraps an [AppError] as a throwable so it can travel through [runCatching]/[Result]. */
class AppException(val error: AppError, cause: Throwable? = null) : Exception(cause)
