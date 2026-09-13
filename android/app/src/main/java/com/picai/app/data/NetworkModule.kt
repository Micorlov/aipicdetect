package com.picai.app.data

import com.picai.app.BuildConfig
import java.util.concurrent.TimeUnit
import kotlin.time.Duration.Companion.seconds
import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.kotlinx.serialization.asConverterFactory

/**
 * Builds a [PicaiApiService] for a given base URL. The base URL is
 * user-configurable at runtime (see [SettingsRepository]), so callers should
 * request a fresh service whenever it changes rather than caching one for
 * the app's lifetime.
 */
object NetworkModule {
    // Generous timeouts: Cloud Run's min-instances=0 means the first request
    // after idle can take up to ~60s to cold-start before it even starts
    // responding.
    private val CALL_TIMEOUT = 90.seconds
    private val CONNECT_TIMEOUT = 20.seconds
    private val READ_TIMEOUT = 90.seconds
    private val WRITE_TIMEOUT = 60.seconds

    private val json = Json {
        ignoreUnknownKeys = true
        explicitNulls = false
    }

    private val okHttpClient: OkHttpClient by lazy {
        OkHttpClient.Builder()
            .callTimeout(CALL_TIMEOUT.inWholeMilliseconds, TimeUnit.MILLISECONDS)
            .connectTimeout(CONNECT_TIMEOUT.inWholeMilliseconds, TimeUnit.MILLISECONDS)
            .readTimeout(READ_TIMEOUT.inWholeMilliseconds, TimeUnit.MILLISECONDS)
            .writeTimeout(WRITE_TIMEOUT.inWholeMilliseconds, TimeUnit.MILLISECONDS)
            .apply {
                if (BuildConfig.DEBUG) {
                    addInterceptor(HttpLoggingInterceptor().setLevel(HttpLoggingInterceptor.Level.BASIC))
                }
            }
            .build()
    }

    fun apiServiceFor(baseUrl: String): PicaiApiService {
        val normalized = if (baseUrl.endsWith("/")) baseUrl else "$baseUrl/"
        val retrofit = Retrofit.Builder()
            .baseUrl(normalized)
            .client(okHttpClient)
            .addConverterFactory(json.asConverterFactory("application/json".toMediaType()))
            .build()
        return retrofit.create(PicaiApiService::class.java)
    }
}
