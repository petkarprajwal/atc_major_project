#!/usr/bin/env python3
"""
Quick Fix Script for Test Failures
Installs missing dependencies and fixes common issues
"""

import subprocess
import sys
import os
from pathlib import Path

def install_missing_packages():
    """Install any missing packages"""
    print("🔧 Installing missing dependencies...")
    
    packages = [
        'python-dotenv',
        'streamlit', 
        'pandas',
        'numpy', 
        'scikit-learn',
        'plotly',
        'folium',
        'requests',
        'websockets',
        'aiohttp'
    ]
    
    for package in packages:
        try:
            print(f"📦 Installing {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'install', package], 
                         check=True, capture_output=True)
            print(f"✅ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"⚠️  {package} installation failed (may already be installed)")
    
    print("✅ Package installation complete!")

def create_missing_files():
    """Create any missing files"""
    print("\n📁 Creating missing files...")
    
    project_dir = Path(__file__).parent
    
    # Create tests/__init__.py if missing
    tests_init = project_dir / "tests" / "__init__.py"
    if not tests_init.exists():
        tests_init.parent.mkdir(exist_ok=True)
        tests_init.write_text('"""Test package for ATC AI System"""')
        print("✅ Created tests/__init__.py")
    
    # Create .env.example if missing
    env_example = project_dir / ".env.example"
    if not env_example.exists():
        env_content = """# OpenSky Network (Free)
OPENSKY_USERNAME=your_username
OPENSKY_PASSWORD=your_password

# OpenWeatherMap (Free)
OPENWEATHER_API_KEY=your_api_key

# Commercial APIs (Optional)
AVIATIONSTACK_API_KEY=your_key
FLIGHTAWARE_API_KEY=your_key
RAPIDAPI_KEY=your_key

# Real-time Settings
WEBSOCKET_ENABLED=True
WEBSOCKET_PORT=8765
UPDATE_INTERVAL=2
"""
        env_example.write_text(env_content)
        print("✅ Created .env.example")
    
    print("✅ File creation complete!")

def main():
    """Run all fixes"""
    print("🛠️  ATC System Quick Fix")
    print("=" * 50)
    
    # Install packages
    install_missing_packages()
    
    # Create missing files
    create_missing_files()
    
    print("\n🎉 All fixes applied!")
    print("\n🧪 Run the test again:")
    print("   python test_enhanced_system.py")
    print("\n🚀 Or launch the dashboard:")
    print("   streamlit run dashboard/realtime_main.py")

if __name__ == "__main__":
    main()
