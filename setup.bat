@echo off
REM Setup script for ATC AI System on Windows

echo ==========================================
echo ATC AI SYSTEM SETUP
echo ==========================================

echo.
echo Creating Python virtual environment...
python -m venv venv

echo.
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing required packages...
pip install -r requirements.txt

echo.
echo Creating environment file...
if not exist .env (
    copy .env.example .env
    echo Created .env file from template
    echo Please edit .env file with your API credentials
) else (
    echo .env file already exists
)

echo.
echo Running system tests...
python test_system.py

echo.
echo ==========================================
echo SETUP COMPLETE!
echo ==========================================
echo.
echo Next steps:
echo 1. Edit .env file with your API credentials
echo 2. Run: streamlit run dashboard\main.py
echo.
echo API Credentials needed:
echo - OpenSky Network: username/password
echo - OpenWeatherMap: API key
echo.
pause
