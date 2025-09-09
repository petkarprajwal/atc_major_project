#!/usr/bin/env python3
"""
Real-time ATC Dashboard Launcher
Launches the enhanced real-time dashboard with proper error handling
"""

import sys
import subprocess
import os
from pathlib import Path

def main():
    """Launch the real-time dashboard"""
    
    # Get the project directory
    project_dir = Path(__file__).parent
    dashboard_path = project_dir / "dashboard" / "realtime_main.py"
    
    print("🚀 Starting Enhanced Real-time ATC Dashboard...")
    print(f"📁 Project Directory: {project_dir}")
    print(f"🎯 Dashboard Path: {dashboard_path}")
    
    # Check if dashboard exists
    if not dashboard_path.exists():
        print(f"❌ Error: Dashboard file not found: {dashboard_path}")
        return 1
    
    # Set environment
    os.chdir(project_dir)
    
    try:
        # Launch Streamlit
        print("🔥 Launching Streamlit...")
        print("📍 Dashboard will be available at: http://localhost:8501")
        print("⚡ WebSocket server will start at: ws://localhost:8765")
        print("🎮 Use Ctrl+C to stop the server")
        print("-" * 60)
        
        # Run streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            str(dashboard_path),
            "--server.headless=true",
            "--server.enableCORS=false"
        ], check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Shutting down dashboard...")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"❌ Error launching dashboard: {e}")
        return 1
    except Exception as e:
        print(f"💥 Unexpected error: {e}")
        return 1

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
