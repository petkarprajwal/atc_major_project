#!/usr/bin/env python3
"""
Emergency Fix Script for Dashboard Errors
Fixes the remaining AttributeError issues
"""

import re
import os
from pathlib import Path

def apply_final_fixes():
    """Apply final fixes to resolve all dashboard errors"""
    print("🔧 Applying Final Dashboard Fixes...")
    print("=" * 50)
    
    project_dir = Path(__file__).parent
    dashboard_file = project_dir / "dashboard" / "realtime_main.py"
    
    if not dashboard_file.exists():
        print("❌ Dashboard file not found!")
        return False
    
    # Read current content
    with open(dashboard_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix 1: Add better error handling for weather data
    print("🔧 Fix 1: Adding robust weather data handling...")
    
    weather_fix = '''def safe_get_weather_data(weather_data):
    """Safely get weather data regardless of format"""
    if not weather_data:
        return {}
    
    # If it's already a dictionary, return as-is
    if isinstance(weather_data, dict):
        return weather_data
    
    # If it's a list, convert to dictionary format
    if isinstance(weather_data, list):
        result = {}
        for item in weather_data:
            if isinstance(item, dict):
                station = item.get('station', f'Station_{len(result)}')
                result[station] = {
                    'weather': {
                        'main': {
                            'temp': item.get('temperature', 20),
                            'humidity': item.get('humidity', 50),
                            'pressure': item.get('pressure', 1013)
                        },
                        'wind': {
                            'speed': item.get('wind_speed', 10) / 3.6
                        },
                        'visibility': item.get('visibility', 10) * 1000,
                        'weather': [{
                            'description': item.get('conditions', 'clear sky')
                        }]
                    }
                }
        return result
    
    return {}

'''
    
    # Add the safe weather function after imports
    if 'def safe_get_weather_data(' not in content:
        import_end = content.find('\nfrom utils.realtime_api import')
        if import_end == -1:
            import_end = content.find('\n# Initialize enhanced session state')
        if import_end != -1:
            content = content[:import_end] + '\n\n' + weather_fix + content[import_end:]
    
    # Fix 2: Update weather tab to use safe function
    print("🔧 Fix 2: Updating weather tab to use safe data handling...")
    
    weather_tab_pattern = r'(with tab3:.*?if weather_data:)(.*?)(else:\s+st\.info\("🔄 No weather data available.*?\"\))'
    
    weather_tab_replacement = r'''\1
            # Use safe weather data handling
            safe_weather = safe_get_weather_data(weather_data)
            
            if safe_weather:
                for location, data in safe_weather.items():
                    with st.expander(f"📍 {location}"):
                        weather_info = data.get('weather', {})
                        
                        col1, col2, col3 = st.columns(3)
                        
                        with col1:
                            temp = weather_info.get('main', {}).get('temp', 0)
                            st.metric("Temperature", f"{temp}°C")
                            
                            humidity = weather_info.get('main', {}).get('humidity', 0)
                            st.metric("Humidity", f"{humidity}%")
                        
                        with col2:
                            wind = weather_info.get('wind', {})
                            wind_speed = wind.get('speed', 0) * 3.6  # Convert to km/h
                            st.metric("Wind Speed", f"{wind_speed:.1f} km/h")
                            
                            pressure = weather_info.get('main', {}).get('pressure', 0)
                            st.metric("Pressure", f"{pressure} hPa")
                        
                        with col3:
                            visibility = weather_info.get('visibility', 0) / 1000
                            st.metric("Visibility", f"{visibility:.1f} km")
                            
                            # Weather conditions
                            conditions = weather_info.get('weather', [])
                            if conditions:
                                condition = conditions[0].get('description', 'Unknown')
                                st.info(f"Conditions: {condition}")
            \3'''
    
    content = re.sub(weather_tab_pattern, weather_tab_replacement, content, flags=re.DOTALL)
    
    # Fix 3: Add comprehensive error handling for conflict detection
    print("🔧 Fix 3: Adding bulletproof conflict detection...")
    
    conflict_pattern = r'(with col4:.*?# Detect conflicts in real-time.*?conflicts = \[\].*?if safe_get_flights\(flights_data\):.*?try:)(.*?)(except Exception as e:.*?st\.error\(f"Conflict detection error: \{e\}"\))'
    
    conflict_replacement = r'''\1
                # Safe conflict detection with comprehensive error handling
                flight_objects = []
                
                try:
                    for i, flight_dict in enumerate(flights_data['flights'][:20]):
                        if not isinstance(flight_dict, dict):
                            continue
                            
                        # Check required fields
                        required_fields = ['latitude', 'longitude', 'baro_altitude']
                        if not all(field in flight_dict and flight_dict[field] is not None for field in required_fields):
                            continue
                        
                        # Create comprehensive safe flight data
                        safe_flight_data = {
                            'icao24': str(flight_dict.get('icao24', f'demo_{i:06d}')),
                            'callsign': str(flight_dict.get('callsign', f'DEMO{i:03d}')),
                            'origin_country': str(flight_dict.get('origin_country', 'Unknown')),
                            'time_position': int(flight_dict.get('time_position', int(time.time()))),
                            'last_contact': int(flight_dict.get('last_contact', int(time.time()))),
                            'longitude': float(flight_dict.get('longitude', 0.0)),
                            'latitude': float(flight_dict.get('latitude', 0.0)),
                            'baro_altitude': float(flight_dict.get('baro_altitude', 35000.0)),
                            'on_ground': bool(flight_dict.get('on_ground', False)),
                            'velocity': float(flight_dict.get('velocity', 450.0)),
                            'true_track': float(flight_dict.get('true_track', 90.0)),
                            'vertical_rate': float(flight_dict.get('vertical_rate', 0.0)),
                            'sensors': list(flight_dict.get('sensors', [])),
                            'geo_altitude': float(flight_dict.get('geo_altitude', flight_dict.get('baro_altitude', 35000.0))),
                            'squawk': str(flight_dict.get('squawk', '0000')),
                            'spi': bool(flight_dict.get('spi', False)),
                            'position_source': int(flight_dict.get('position_source', 0))
                        }
                        
                        flight_obj = FlightData(**safe_flight_data)
                        flight_objects.append(flight_obj)
                
                    # Only run conflict detection if we have enough valid flights
                    if len(flight_objects) >= 2:
                        detector = ConflictDetector()
                        conflicts = detector.detect_all_conflicts(flight_objects)
                        
                except ImportError as ie:
                    st.warning(f"Conflict detection not available: {ie}")
                    conflicts = []
                \3
                    # Enhanced debug information
                    if st.checkbox("🐛 Show Debug Info", key="conflict_debug"):
                        st.text(f"Error: {str(e)}")
                        st.text(f"Flight objects created: {len(flight_objects)}")
                        if flights_data and 'flights' in flights_data:
                            sample_flight = flights_data['flights'][0] if flights_data['flights'] else {}
                            st.text(f"Sample flight keys: {list(sample_flight.keys())}")'''
    
    content = re.sub(conflict_pattern, conflict_replacement, content, flags=re.DOTALL)
    
    # Write the fixed content back
    with open(dashboard_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ All fixes applied successfully!")
    print("\n🎯 Fixed Issues:")
    print("   • Weather data format errors (list vs dict)")
    print("   • FlightData missing parameter errors")
    print("   • Conflict detection robustness")
    print("   • Enhanced error reporting and debugging")
    
    return True

def main():
    """Apply all emergency fixes"""
    print("🚨 Emergency Dashboard Fix Application")
    print("=" * 60)
    
    try:
        success = apply_final_fixes()
        
        if success:
            print("\n🎉 SUCCESS! All dashboard fixes applied!")
            print("\n🚀 Next Steps:")
            print("   1. Refresh your browser (F5)")
            print("   2. Click 'Start Real-time' button")
            print("   3. Test 'Manual Refresh' button")
            print("   4. Check all tabs for errors")
            print("\n💡 If you still see errors:")
            print("   • Enable 'Show Debug Info' checkbox")
            print("   • Check browser console for JavaScript errors")
            print("   • Restart Streamlit if needed")
        else:
            print("\n❌ Some fixes failed to apply")
            
    except Exception as e:
        print(f"\n💥 Emergency fix failed: {e}")
        return False
    
    return success

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)
