package com.aipicdetect.app.data

/** Canonical doc-page paths, the repo URL and the Play listing, per src/aipicdetect/pages.py. */
object AppLinks {
    const val REPO_URL = "https://github.com/Micorlov/aipicdetect"

    const val PLAY_PACKAGE = "com.aipicdetect.app"

    /** Opens the Play Store app directly; falls back to [PLAY_WEB_URL] when it isn't installed. */
    const val PLAY_MARKET_URI = "market://details?id=$PLAY_PACKAGE"
    const val PLAY_WEB_URL = "https://play.google.com/store/apps/details?id=$PLAY_PACKAGE"

    fun page(baseUrl: String, path: String): String {
        val trimmed = baseUrl.trimEnd('/')
        return "$trimmed$path"
    }
}
