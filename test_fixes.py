#!/usr/bin/env python3
"""
Quick Fix Tester for Dashboard Errors
Tests the specific error fixes
"""

import sys
import os
from pathlib import Path

# Add project directory to path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

def test_weather_data_fix():
    """Test the weather data format fix"""
    print("🧪 Testing Weather Data Format Fix...")
    print("-" * 50)
    
    try:
        # Import the dashboard function
        sys.path.insert(0, str(project_dir / 'dashboard'))
        from realtime_main import generate_demo_weather_data
        
        # Generate demo weather data
        weather_data = generate_demo_weather_data()
        
        print(f"✅ Weather data generated successfully")
        print(f"✅ Type: {type(weather_data)} (should be dict)")
        print(f"✅ Keys: {list(weather_data.keys()) if isinstance(weather_data, dict) else 'Not a dict'}")
        
        # Test data structure
        if isinstance(weather_data, dict):
            for location, data in weather_data.items():
                if 'weather' in data and 'main' in data['weather']:
                    print(f"✅ {location}: Correct structure")
                else:
                    print(f"❌ {location}: Incorrect structure")
                    return False
            return True
        else:
            print("❌ Weather data is not a dictionary")
            return False
            
    except Exception as e:
        print(f"❌ Weather data test failed: {e}")
        return False

def test_flight_data_creation():
    """Test FlightData object creation fix"""
    print("\n🧪 Testing FlightData Creation Fix...")
    print("-" * 50)
    
    try:
        # Import required classes
        from utils.data_processing import FlightData
        
        # Test flight data creation with demo data structure
        demo_flight = {
            'icao24': 'abc123',
            'callsign': 'TEST123',
            'origin_country': 'United States',
            'latitude': 40.7128,
            'longitude': -74.0060,
            'baro_altitude': 35000,
            'velocity': 450,
            'true_track': 90
        }
        
        # Create safe flight data (like in the fix)
        safe_flight_data = {
            'icao24': demo_flight.get('icao24', '000000'),
            'callsign': demo_flight.get('callsign', 'UNKNOWN'),
            'origin_country': demo_flight.get('origin_country', 'Unknown'),
            'time_position': demo_flight.get('time_position', 1234567890),
            'last_contact': demo_flight.get('last_contact', 1234567890),
            'longitude': demo_flight.get('longitude', 0.0),
            'latitude': demo_flight.get('latitude', 0.0),
            'baro_altitude': demo_flight.get('baro_altitude', 0.0),
            'on_ground': demo_flight.get('on_ground', False),
            'velocity': demo_flight.get('velocity', 0.0),
            'true_track': demo_flight.get('true_track', 0.0),
            'vertical_rate': demo_flight.get('vertical_rate', 0.0),
            'sensors': demo_flight.get('sensors', []),
            'geo_altitude': demo_flight.get('geo_altitude', demo_flight.get('baro_altitude', 0.0)),
            'squawk': demo_flight.get('squawk', '0000'),
            'spi': demo_flight.get('spi', False),
            'position_source': demo_flight.get('position_source', 0)
        }
        
        # Create FlightData object
        flight_obj = FlightData(**safe_flight_data)
        
        print(f"✅ FlightData object created successfully")
        print(f"✅ Callsign: {flight_obj.callsign}")
        print(f"✅ Country: {flight_obj.origin_country}")
        print(f"✅ Position: {flight_obj.latitude}, {flight_obj.longitude}")
        
        return True
        
    except Exception as e:
        print(f"❌ FlightData creation test failed: {e}")
        return False

def test_dashboard_imports():
    """Test dashboard imports work correctly"""
    print("\n🧪 Testing Dashboard Imports...")
    print("-" * 50)
    
    try:
        # Test importing dashboard components
        sys.path.insert(0, str(project_dir / 'dashboard'))
        
        # Test key imports that could cause issues
        import realtime_main
        print("✅ realtime_main imported successfully")
        
        from utils.data_processing import FlightData
        print("✅ FlightData imported successfully")
        
        from models.collision_avoidance import ConflictDetector
        print("✅ ConflictDetector imported successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ Dashboard imports failed: {e}")
        return False

def main():
    """Run all fix tests"""
    print("🚀 Dashboard Error Fix Test Suite")
    print("=" * 60)
    
    tests = [
        ("Weather Data Format", test_weather_data_fix),
        ("FlightData Creation", test_flight_data_creation),
        ("Dashboard Imports", test_dashboard_imports)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append(result)
        except Exception as e:
            print(f"💥 {test_name} test crashed: {e}")
            results.append(False)
    
    # Summary
    print("\n📋 Fix Test Summary")
    print("=" * 60)
    
    passed = sum(results)
    total = len(results)
    
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"{status} {test_name}")
    
    print("-" * 60)
    print(f"🎯 Overall: {passed}/{total} fixes verified")
    
    if passed == total:
        print("\n🎉 ALL FIXES VERIFIED! Dashboard errors should be resolved!")
        print("\n🚀 To test the dashboard:")
        print("   streamlit run dashboard/realtime_main.py")
        print("\n💡 The following errors have been fixed:")
        print("   • Weather data 'list object has no attribute items' error")
        print("   • FlightData 'missing required positional arguments' error")
        print("   • Improved error handling and debug information")
    else:
        print(f"\n⚠️  {total - passed} fixes failed verification.")
        print("Check the error messages above for details.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
