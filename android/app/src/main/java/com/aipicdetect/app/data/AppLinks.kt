package com.aipicdetect.app.data

/** Canonical doc-page paths and the repo URL, per src/aipicdetect/pages.py's page registry. */
object AppLinks {
    const val REPO_URL = "https://github.com/Micorlov/aipicdetect"

    fun page(baseUrl: String, path: String): String {
        val trimmed = baseUrl.trimEnd('/')
        return "$trimmed$path"
    }
}
