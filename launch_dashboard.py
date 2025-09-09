#!/usr/bin/env python3
"""
Dashboard Connection Troubleshooter
Helps diagnose and fix connection issues
"""

import socket
import subprocess
import sys
import webbrowser
from pathlib import Path

def check_port(port, host='localhost'):
    """Check if a port is available"""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            return result == 0
    except:
        return False

def find_available_port(start_port=8501):
    """Find an available port starting from start_port"""
    for port in range(start_port, start_port + 10):
        if not check_port(port):
            return port
    return None

def launch_dashboard():
    """Launch the dashboard with proper error handling"""
    print("🚀 Enhanced ATC Dashboard Launcher")
    print("=" * 50)
    
    # Check project structure
    project_dir = Path(__file__).parent
    dashboard_file = project_dir / "dashboard" / "realtime_main.py"
    
    if not dashboard_file.exists():
        print("❌ Error: Dashboard file not found!")
        print(f"   Expected: {dashboard_file}")
        return False
    
    print("✅ Dashboard file found")
    
    # Check if default port is available
    default_port = 8501
    if check_port(default_port):
        print(f"⚠️  Port {default_port} is already in use")
        available_port = find_available_port(8502)
        if available_port:
            print(f"🔄 Using alternative port: {available_port}")
            port_arg = f"--server.port {available_port}"
        else:
            print("❌ No available ports found")
            return False
    else:
        print(f"✅ Port {default_port} is available")
        available_port = default_port
        port_arg = ""
    
    # Launch Streamlit
    try:
        print(f"\n🌐 Dashboard will be available at: http://localhost:{available_port}")
        print("⚡ WebSocket server will start automatically")
        print("🎮 Press Ctrl+C to stop the server")
        print("-" * 50)
        
        # Build command
        cmd = [
            sys.executable, "-m", "streamlit", "run", 
            str(dashboard_file),
            "--server.headless=false"
        ]
        
        if port_arg:
            cmd.extend(port_arg.split())
        
        # Launch in a way that opens browser
        subprocess.run(cmd, cwd=str(project_dir))
        
    except KeyboardInterrupt:
        print("\n🛑 Dashboard stopped by user")
        return True
    except FileNotFoundError:
        print("❌ Error: Streamlit not found. Install with: pip install streamlit")
        return False
    except Exception as e:
        print(f"❌ Error launching dashboard: {e}")
        return False

def main():
    """Main function"""
    success = launch_dashboard()
    
    if not success:
        print("\n🔧 Troubleshooting Tips:")
        print("1. Install Streamlit: pip install streamlit")
        print("2. Check firewall settings")
        print("3. Try different port: streamlit run dashboard/realtime_main.py --server.port 8502")
        print("4. Check antivirus software")
        
        # Try opening browser manually
        try:
            print("\n🌐 Trying to open browser manually...")
            webbrowser.open("http://localhost:8501")
        except:
            pass

if __name__ == "__main__":
    main()
