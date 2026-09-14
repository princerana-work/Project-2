[app]

# (str) Title of your application
title = Music Streamer

# (str) Package name
package.name = musicstreamer

# (str) Package domain
package.domain = org.test

# (str) Source code directory
source.dir = .

# (str) Application version
version = 0.1

# (list) Source files
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy,openssl,requests

# (list) Supported orientations
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (int) Target Android API (Recommended API 33)
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android NDK version recommended by p4a
android.ndk = 25c

# (bool) Accept NDK license automatically
android.accept_sdk_license = True

# Allow HTTP cleartext traffic
android.manifest.application_arguments = android:usesCleartextTraffic="true"

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

[buildozer]

# Log level
log_level = 2

# Warn on root
warn_on_root = 1
