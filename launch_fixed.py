#!/usr/bin/env python3
"""
Fixed Dashboard Launcher
Handles import issues and launches the dashboard properly
"""

import sys
import os
from pathlib import Path

def setup_paths():
    """Setup Python paths for proper imports"""
    project_dir = Path(__file__).parent
    
    # Add project directory to Python path
    if str(project_dir) not in sys.path:
        sys.path.insert(0, str(project_dir))
    
    # Change working directory
    os.chdir(project_dir)

def main():
    """Launch the dashboard with proper setup"""
    print("🔧 Setting up environment...")
    setup_paths()
    
    print("🚀 Launching Enhanced Real-time ATC Dashboard...")
    print("📍 Dashboard will be available at: http://localhost:8501")
    print("⚡ WebSocket server will start at: ws://localhost:8765")
    print("-" * 60)
    
    # Import and run streamlit
    try:
        import subprocess
        
        # Launch streamlit with proper environment
        env = os.environ.copy()
        env['PYTHONPATH'] = str(Path(__file__).parent)
        
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "dashboard/realtime_main.py",
            "--server.headless=false"
        ], env=env, check=True)
        
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Try manual launch:")
        print("   streamlit run dashboard/realtime_main.py")

if __name__ == "__main__":
    main()
