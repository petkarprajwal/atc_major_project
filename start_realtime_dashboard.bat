@echo off
echo ========================================
echo   🚀 Enhanced Real-time ATC Dashboard
echo ========================================
echo.
echo Starting the AI-powered Air Traffic Control system...
echo Dashboard will be available at: http://localhost:8501
echo WebSocket server will start at: ws://localhost:8765
echo.
echo Press Ctrl+C to stop the server
echo.
echo ----------------------------------------

cd /d "%~dp0"
python -m streamlit run dashboard\realtime_main.py --server.headless=true --server.enableCORS=false

pause
