package com.aipicdetect.app.data

import android.content.Context
import androidx.datastore.preferences.preferencesDataStore

/**
 * The app's single Preferences DataStore.
 *
 * Declared in one place on purpose: the delegate installs a process-wide singleton per file
 * name, so a second `preferencesDataStore(name = "settings")` elsewhere would throw at runtime.
 * The name matches the original store so existing installs keep their saved base URL.
 */
internal val Context.appDataStore by preferencesDataStore(name = "settings")
