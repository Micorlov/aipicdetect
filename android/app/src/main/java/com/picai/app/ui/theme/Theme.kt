package com.picai.app.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

/** picai's site is dark-only (color-scheme: dark, no prefers-color-scheme block) — one canonical theme. */
private val PicaiColorScheme = darkColorScheme(
    primary = Accent,
    onPrimary = OnAccent,
    secondary = Success,
    tertiary = Warn,
    background = Background,
    onBackground = TextPrimary,
    surface = Surface,
    onSurface = TextPrimary,
    surfaceVariant = SurfaceVariant,
    onSurfaceVariant = TextMuted,
    outline = Border,
    error = Danger,
    onError = TextPrimary,
    errorContainer = Danger.copy(alpha = 0.14f),
    onErrorContainer = Danger,
)

@Composable
fun PicaiTheme(content: @Composable () -> Unit) {
    MaterialTheme(colorScheme = PicaiColorScheme, typography = PicaiTypography, content = content)
}
