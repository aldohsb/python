@echo off
REM Build Script untuk Minimalist Timer Application
REM Script ini akan membuat executable dari aplikasi timer

echo ========================================
echo Minimalist Timer - Build Script
echo ========================================
echo.

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller tidak ditemukan. Installing...
    pip install pyinstaller
    echo.
)

echo Memulai build process...
echo.

REM Clean previous builds
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "*.spec" del /q *.spec

echo Cleaning completed.
echo.

REM Build executable
echo Building executable...
pyinstaller --onefile --windowed --name "MinimalTimer" timer_app.py

echo.
if errorlevel 1 (
    echo Build GAGAL! Cek error di atas.
    pause
    exit /b 1
)

echo ========================================
echo Build BERHASIL!
echo ========================================
echo.
echo Executable file: dist\MinimalTimer.exe
echo.
echo Kamu bisa:
echo 1. Run executable: cd dist ^&^& MinimalTimer.exe
echo 2. Copy file .exe ke lokasi lain
echo 3. Bagikan file .exe ke orang lain
echo.
pause
