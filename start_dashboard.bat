@echo off
echo.
echo 🚀 Starting Enhanced Real-time ATC Dashboard...
echo.
echo 📍 Dashboard will be available at: http://localhost:8503
echo ⚡ WebSocket server will start at: ws://localhost:8765
echo 🎮 Use Ctrl+C to stop the server
echo.
echo ----------------------------------------
cd /d "c:\Users\Petka\Desktop\ATC\atc_ai_project"
set PYTHONPATH=%CD%
python -m streamlit run dashboard/realtime_main.py --server.port=8503 --server.headless=false
pause
