@echo off
setlocal
cd /d "%~dp0"
where flutter >nul 2>nul
if errorlevel 1 (
  echo Flutter was not found in PATH.
  echo Install Flutter SDK and add flutter\bin to PATH, then reopen this window.
  pause
  exit /b 1
)

echo Checking Flutter installation...
flutter --version
if errorlevel 1 exit /b 1

echo Repairing/regenerating missing Flutter platform files if needed...
flutter create .
if errorlevel 1 exit /b 1

echo Getting packages...
flutter pub get
if errorlevel 1 exit /b 1

echo Building release APK...
flutter build apk --release
if errorlevel 1 exit /b 1

echo.
echo APK created at:
echo build\app\outputs\flutter-apk\app-release.apk
pause
