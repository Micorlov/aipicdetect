package com.aipicdetect.app

import android.app.Application
import com.aipicdetect.app.data.DataStoreEngagementRepository
import com.aipicdetect.app.data.DataStoreSettingsRepository
import com.aipicdetect.app.data.EngagementRepository
import com.aipicdetect.app.data.AiPicDetectRepository
import com.aipicdetect.app.data.AiPicDetectRepositoryImpl
import com.aipicdetect.app.data.SettingsRepository

/** Minimal manual DI container — the app is small enough that a framework isn't warranted. */
class AiPicDetectApp : Application() {
    val settingsRepository: SettingsRepository by lazy { DataStoreSettingsRepository(this) }
    val engagementRepository: EngagementRepository by lazy { DataStoreEngagementRepository(this) }
    val aiPicDetectRepository: AiPicDetectRepository by lazy { AiPicDetectRepositoryImpl(this, settingsRepository) }
}
