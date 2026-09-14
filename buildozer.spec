[app]

# (str) Title of your application
title = Music Streamer

# (str) Package name
package.name = musicstreamer
# (str) Application versioning
version = 0.1

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# openssl and urllib3 are required for HTTPS API requests and audio stream buffering
requirements = python3,kivy,openssl,urllib3,requests

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Internet permissions are strictly mandatory for music streaming
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Accept NDK license automatically
android.accept_sdk_license = True

# Allows HTTP cleartext traffic for media streaming
android.manifest.application_arguments = android:usesCleartextTraffic="true"

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Architectures to build for (64-bit and 32-bit ARM for modern devices)
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup of application data
android.allow_backup = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
