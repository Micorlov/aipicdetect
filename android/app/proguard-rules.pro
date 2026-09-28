# Play Core's review-ktx references a Play Services annotation that is not on the
# compile classpath. It is annotation-only and never needed at runtime, so R8 can
# safely be told to stop warning about it — without this the release build fails.
-dontwarn com.google.android.gms.common.annotation.NoNullnessRewrite
