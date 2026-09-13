package com.picai.app

import android.app.Application
import com.picai.app.data.DataStoreSettingsRepository
import com.picai.app.data.PicaiRepository
import com.picai.app.data.PicaiRepositoryImpl
import com.picai.app.data.SettingsRepository

/** Minimal manual DI container — the app is small enough that a framework isn't warranted. */
class PicaiApp : Application() {
    val settingsRepository: SettingsRepository by lazy { DataStoreSettingsRepository(this) }
    val picaiRepository: PicaiRepository by lazy { PicaiRepositoryImpl(this, settingsRepository) }
}
