package com.aipicdetect.app.data

import android.content.Context
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.intPreferencesKey
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.flow.map

/**
 * Successful analyses a user must complete before the in-app review prompt is offered.
 * Asking before someone has seen a result twice over produces uninformed ratings.
 */
const val REVIEW_PROMPT_THRESHOLD = 3

private val ONBOARDING_SEEN_KEY = booleanPreferencesKey("onboarding_seen")
private val ANALYSIS_COUNT_KEY = intPreferencesKey("successful_analyses")
private val REVIEW_OFFERED_KEY = booleanPreferencesKey("review_offered")

/** First-run and review-prompt state — the bookkeeping behind onboarding and rating. */
interface EngagementRepository {
    val hasSeenOnboarding: Flow<Boolean>
    suspend fun markOnboardingSeen()
    suspend fun recordSuccessfulAnalysis()
    suspend fun shouldOfferReview(): Boolean
    suspend fun markReviewOffered()
}

class DataStoreEngagementRepository(private val context: Context) : EngagementRepository {

    override val hasSeenOnboarding: Flow<Boolean> =
        context.appDataStore.data.map { prefs -> prefs[ONBOARDING_SEEN_KEY] ?: false }

    override suspend fun markOnboardingSeen() {
        context.appDataStore.edit { prefs -> prefs[ONBOARDING_SEEN_KEY] = true }
    }

    override suspend fun recordSuccessfulAnalysis() {
        context.appDataStore.edit { prefs ->
            prefs[ANALYSIS_COUNT_KEY] = (prefs[ANALYSIS_COUNT_KEY] ?: 0) + 1
        }
    }

    override suspend fun shouldOfferReview(): Boolean {
        val prefs = context.appDataStore.data.first()
        val alreadyOffered = prefs[REVIEW_OFFERED_KEY] ?: false
        val analyses = prefs[ANALYSIS_COUNT_KEY] ?: 0
        return !alreadyOffered && analyses >= REVIEW_PROMPT_THRESHOLD
    }

    override suspend fun markReviewOffered() {
        context.appDataStore.edit { prefs -> prefs[REVIEW_OFFERED_KEY] = true }
    }
}
