package com.aipicdetect.app.util

import android.app.Activity
import android.content.ActivityNotFoundException
import android.content.Context
import android.content.ContextWrapper
import android.content.Intent
import android.net.Uri
import com.aipicdetect.app.data.AppLinks
import com.google.android.play.core.ktx.launchReview
import com.google.android.play.core.ktx.requestReview
import com.google.android.play.core.review.ReviewManagerFactory

/** Unwraps the [Activity] behind a Compose `LocalContext`, which is usually a ContextWrapper. */
fun Context.findActivity(): Activity? {
    var current = this
    while (current is ContextWrapper) {
        if (current is Activity) return current
        current = current.baseContext
    }
    return null
}

/**
 * Asks Play to show its in-app review card.
 *
 * Whether the card actually appears is entirely Play's decision — it silently does nothing
 * when the user has already rated, or when the per-user quota is spent. That is by design,
 * so a failure here is never surfaced to the user; the explicit "Rate this app" button in
 * Settings is the path that always works.
 */
suspend fun launchInAppReview(activity: Activity): Boolean = runCatching {
    val manager = ReviewManagerFactory.create(activity)
    manager.launchReview(activity, manager.requestReview())
    true
}.getOrDefault(false)

/** Opens the Play listing, preferring the installed Play app over the browser. */
fun openPlayStoreListing(context: Context) {
    val market = Intent(Intent.ACTION_VIEW, Uri.parse(AppLinks.PLAY_MARKET_URI))
        .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
    try {
        context.startActivity(market)
    } catch (_: ActivityNotFoundException) {
        context.startActivity(
            Intent(Intent.ACTION_VIEW, Uri.parse(AppLinks.PLAY_WEB_URL))
                .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK),
        )
    }
}
