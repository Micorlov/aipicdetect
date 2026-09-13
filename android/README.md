# picai Android client

A thin native Android client for the [picai](../README.md) API: pick or take a photo,
send it to `/analyze`, see the AI-likelihood score and what metadata was found, then
save or share the scrubbed copy.

## Stack

Kotlin + Jetpack Compose (Material 3), Retrofit/OkHttp + kotlinx.serialization,
Jetpack DataStore for the settings override. No DI framework — `PicaiApp` is a small
manual container, small enough not to need one.

## Requirements

- Android Studio (or the command line tools) with SDK platform **36** and
  build-tools **36.x** installed.
- JDK 17.

## Build & test

```bash
cd android
./gradlew testDebugUnitTest   # repository / error-mapping / DTO / ViewModel tests
./gradlew assembleDebug       # app/build/outputs/apk/debug/app-debug.apk
```

`local.properties` (git-ignored) must point `sdk.dir` at your Android SDK — Android
Studio creates this for you on first open; from the command line:

```bash
echo "sdk.dir=$ANDROID_HOME" > local.properties
```

## Pointing at a different server

The app defaults to the production Cloud Run instance
(`https://picai-53480028562.europe-west1.run.app`). To point it at a local dev server
instead, open the app's **Settings** (gear icon in the top bar) and set the base URL —
e.g. `http://10.0.2.2:8000` for an emulator talking to `uv run picai serve` on the host.
Cleartext HTTP is only permitted for `10.0.2.2`/`localhost`/`127.0.0.1`
(see `network_security_config.xml`); the production URL stays HTTPS-only.

## Notes

- `/analyze` already returns the scrubbed image's `download_url`, so the app never calls
  `/scrub` separately — see [PicaiRepository.kt](app/src/main/java/com/picai/app/data/PicaiRepository.kt).
- Cloud Run's `min-instances=0` means the first request after idle can take up to ~60s;
  the loading screen switches to a "waking up the server" hint after 8s
  (`COLD_START_HINT_DELAY_MILLIS` in [HomeViewModel.kt](app/src/main/java/com/picai/app/ui/home/HomeViewModel.kt)).
