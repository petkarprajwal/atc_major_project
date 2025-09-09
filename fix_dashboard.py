#!/usr/bin/env python3
"""
Quick Fix for flights_data format issues
Fixes the AttributeError in the dashboard
"""

import re
from pathlib import Path

def fix_flights_data_errors():
    """Fix all flights_data.get() calls to handle both dict and list formats"""
    
    dashboard_file = Path("c:/Users/Petka/Desktop/ATC/atc_ai_project/dashboard/realtime_main.py")
    
    print("🔧 Fixing flights_data format issues...")
    
    # Read the file
    content = dashboard_file.read_text(encoding='utf-8')
    
    # Helper function pattern
    helper_function = '''
def safe_get_flights(flights_data):
    """Safely get flights list from data"""
    if isinstance(flights_data, dict):
        return flights_data.get('flights', [])
    elif isinstance(flights_data, list):
        return flights_data
    else:
        return []

def safe_get_sources(flights_data):
    """Safely get sources list from data"""
    if isinstance(flights_data, dict):
        return flights_data.get('sources', [])
    else:
        return ['demo']
'''
    
    # Add helper functions after imports
    import_end = content.find('# Page configuration')
    if import_end != -1:
        content = content[:import_end] + helper_function + '\n' + content[import_end:]
    
    # Replace all flights_data.get('flights') calls
    patterns = [
        (r"flights_data\.get\('flights', \[\]\)", "safe_get_flights(flights_data)"),
        (r"flights_data\.get\('flights'\)", "safe_get_flights(flights_data)"),
        (r"flights_data\.get\('sources', \[\]\)", "safe_get_sources(flights_data)"),
        (r"flights_data\.get\('sources'\)", "safe_get_sources(flights_data)"),
    ]
    
    for pattern, replacement in patterns:
        content = re.sub(pattern, replacement, content)
    
    # Also fix the conditional checks
    content = re.sub(
        r"if flights_data and flights_data\.get\('flights'\):",
        "if flights_data and safe_get_flights(flights_data):",
        content
    )
    
    content = re.sub(
        r"if not flights_data or not flights_data\.get\('flights'\):",
        "if not flights_data or not safe_get_flights(flights_data):",
        content
    )
    
    # Write back the fixed content
    dashboard_file.write_text(content, encoding='utf-8')
    
    print("✅ Fixed all flights_data format issues!")
    print("🔄 Please refresh your browser to see the fixes")

if __name__ == "__main__":
    fix_flights_data_errors()
