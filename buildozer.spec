[app]

# (str) Title of your app
title = Estudos

# (str) Package name
package.name = estudos

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,txt,png,jpg,kv,atlas
source.include_files = topicos.txt

# (list) List of directory to include (let empty to include all the directories)
source.include_dirs = .

# (list) List of exclusions
source.exclude_exts = pyo

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) List of service to declare
android.permissions = INTERNET

# (str) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 19c

# (str) Release mode? (True or False)
android.release = debug

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
android.copy_libs = 1

# (str) The Android app's main Python file
android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported android version
android.api = 30

# (int) Android min API to use
android.minapi = 21

# (str) Android NDK API to use. This is the minimum API your app will support, it should usually match android.minapi
android.ndk_api = 21

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android architecture to use (armeabi-v7l, arm64-v8a, x86)
android.arch = armeabi-v7l

source.dir = .

version = 1.0

# (str) Main entry point of the application
main.py = Estudos.py
