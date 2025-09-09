#!/usr/bin/env python3
"""
Direct Dashboard Launcher
Launches the dashboard directly without background processes
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Launch the dashboard"""
    print("🚀 Launching Enhanced Real-time ATC Dashboard...")
    print("=" * 60)
    
    # Get project directory
    project_dir = Path(__file__).parent
    dashboard_path = project_dir / "dashboard" / "realtime_main.py"
    
    print(f"📁 Project: {project_dir}")
    print(f"🎯 Dashboard: {dashboard_path}")
    
    # Check if file exists
    if not dashboard_path.exists():
        print(f"❌ Dashboard file not found: {dashboard_path}")
        return
    
    # Change to project directory
    os.chdir(project_dir)
    
    print("\n🌐 Dashboard URLs:")
    print("   Main Dashboard: http://localhost:8501")
    print("   WebSocket:      ws://localhost:8765")
    print("\n⚡ Starting server...")
    print("🎮 Press Ctrl+C to stop")
    print("-" * 60)
    
    # Launch streamlit directly
    try:
        # Use explicit python path and streamlit module
        cmd = [sys.executable, "-m", "streamlit", "run", str(dashboard_path)]
        subprocess.run(cmd, check=True)
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        print("\n💡 Try installing Streamlit:")
        print("   pip install streamlit")
    except FileNotFoundError:
        print("❌ Python or Streamlit not found")
        print("\n💡 Install dependencies:")
        print("   pip install streamlit")

if __name__ == "__main__":
    main()
