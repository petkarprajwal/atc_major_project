#!/usr/bin/env python3
"""
Emergency Dashboard Fix
Fixes recursion and infinite loop errors
"""

import re
from pathlib import Path

def fix_dashboard_errors():
    """Fix critical errors in dashboard"""
    
    dashboard_file = Path("c:/Users/Petka/Desktop/ATC/atc_ai_project/dashboard/realtime_main.py")
    
    print("🔧 Fixing critical dashboard errors...")
    
    # Read the file
    content = dashboard_file.read_text(encoding='utf-8')
    
    # Remove problematic auto-refresh that causes infinite loops
    auto_refresh_pattern = r'# Auto-refresh demo data when streaming is active.*?last_update = current_time'
    content = re.sub(auto_refresh_pattern, '', content, flags=re.DOTALL)
    
    # Fix the manual refresh button to properly populate data
    manual_refresh_section = '''        if st.button("🔄 Manual Refresh", key="manual_refresh"):
            # Fetch data manually
            with st.spinner("Fetching latest data..."):
                # Generate demo data immediately
                demo_flights = generate_demo_flight_data()
                demo_weather = generate_demo_weather_data()
                
                # Update session state
                st.session_state.realtime_data['flights'] = demo_flights
                st.session_state.realtime_data['weather'] = demo_weather
                st.session_state.realtime_data['last_update'] = datetime.now()
                
                st.success("✅ Data refreshed successfully!")
                st.rerun()'''
    
    # Find and replace the manual refresh section
    pattern = r'if st\.button\("🔄 Manual Refresh".*?st\.success\("✅ Data updated successfully!"\)'
    content = re.sub(pattern, manual_refresh_section, content, flags=re.DOTALL)
    
    # Write back the fixed content
    dashboard_file.write_text(content, encoding='utf-8')
    
    print("✅ Fixed recursion and infinite loop errors!")
    print("🔄 Please refresh your browser to see the fixes")

if __name__ == "__main__":
    fix_dashboard_errors()
