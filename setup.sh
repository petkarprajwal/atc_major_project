#!/bin/bash
# Setup script for ATC AI System on Linux/Mac

echo "=========================================="
echo "ATC AI SYSTEM SETUP"
echo "=========================================="

echo
echo "Creating Python virtual environment..."
python3 -m venv venv

echo
echo "Activating virtual environment..."
source venv/bin/activate

echo
echo "Upgrading pip..."
python -m pip install --upgrade pip

echo
echo "Installing required packages..."
pip install -r requirements.txt

echo
echo "Creating environment file..."
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file from template"
    echo "Please edit .env file with your API credentials"
else
    echo ".env file already exists"
fi

echo
echo "Running system tests..."
python test_system.py

echo
echo "=========================================="
echo "SETUP COMPLETE!"
echo "=========================================="
echo
echo "Next steps:"
echo "1. Edit .env file with your API credentials"
echo "2. Run: streamlit run dashboard/main.py"
echo
echo "API Credentials needed:"
echo "- OpenSky Network: username/password"
echo "- OpenWeatherMap: API key"
echo
