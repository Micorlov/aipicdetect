package com.aipicdetect.app.data

import android.content.Context
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import com.aipicdetect.app.BuildConfig
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

private val Context.settingsDataStore by preferencesDataStore(name = "settings")
private val BASE_URL_KEY = stringPreferencesKey("base_url")

interface SettingsRepository {
    val baseUrl: Flow<String>
    suspend fun setBaseUrl(url: String)
    suspend fun resetToDefault()
}

/** Persists the user's API base-URL override (defaults to the production Cloud Run URL). */
class DataStoreSettingsRepository(private val context: Context) : SettingsRepository {

    override val baseUrl: Flow<String> =
        context.settingsDataStore.data.map { prefs ->
            prefs[BASE_URL_KEY]?.takeIf { it.isNotBlank() } ?: BuildConfig.DEFAULT_BASE_URL
        }

    override suspend fun setBaseUrl(url: String) {
        context.settingsDataStore.edit { prefs -> prefs[BASE_URL_KEY] = url.trim() }
    }

    override suspend fun resetToDefault() {
        context.settingsDataStore.edit { prefs -> prefs.remove(BASE_URL_KEY) }
    }
}
