#!/usr/bin/env python3
"""
Manual Demo Data Trigger
Click this to manually add demo data to your dashboard
"""

import sys
from pathlib import Path

# Add project directory to path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

def main():
    print("🎮 Demo Data Trigger")
    print("=" * 40)
    
    # Test demo data generation
    from demo_data import generate_demo_flights, get_demo_weather
    
    print("🧪 Generating demo data...")
    
    flights = generate_demo_flights(15)
    weather = get_demo_weather()
    
    print(f"✅ Generated {len(flights['flights'])} flights")
    print(f"✅ Generated {len(weather)} weather stations")
    
    print("\n📊 Demo Flight Summary:")
    for i, flight in enumerate(flights['flights'][:5]):  # Show first 5
        print(f"  {i+1}. {flight['callsign']} ({flight['origin']} → {flight['destination']})")
        print(f"     Position: {flight['latitude']:.2f}, {flight['longitude']:.2f}")
        print(f"     Altitude: {flight['baro_altitude']} ft")
    
    if len(flights['flights']) > 5:
        print(f"  ... and {len(flights['flights']) - 5} more flights")
    
    print("\n🌤️ Weather Summary:")
    for station in weather:
        print(f"  {station['station']}: {station['temperature']}°C, {station['conditions']}")
    
    print("\n🚀 Instructions:")
    print("1. Go to your browser with the dashboard open")
    print("2. Click 'Start Real-time' if not already started")
    print("3. Click 'Manual Refresh' to update data")
    print("4. You should see the flight count increase!")
    
    print("\n💡 If you still don't see data:")
    print("- Try refreshing the browser page (F5)")
    print("- Check that WebSocket shows 'Connected'")
    print("- Look for the green 'LIVE' indicator")

if __name__ == "__main__":
    main()
