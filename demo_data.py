#!/usr/bin/env python3
"""
Demo Data Generator
Adds realistic demo flight data to the dashboard
"""

import random
import time
from datetime import datetime, timedelta

def generate_demo_flights(count=12):
    """Generate realistic demo flight data"""
    
    # Major airports with coordinates
    airports = {
        'JFK': {'lat': 40.6413, 'lon': -73.7781, 'name': 'John F. Kennedy International'},
        'LAX': {'lat': 33.9425, 'lon': -118.4081, 'name': 'Los Angeles International'},
        'ORD': {'lat': 41.9796, 'lon': -87.9045, 'name': 'Chicago O\'Hare International'},
        'ATL': {'lat': 33.6407, 'lon': -84.4277, 'name': 'Hartsfield-Jackson Atlanta'},
        'DFW': {'lat': 32.8968, 'lon': -97.0380, 'name': 'Dallas Fort Worth International'},
        'DEN': {'lat': 39.8561, 'lon': -104.6737, 'name': 'Denver International'},
        'LAS': {'lat': 36.0840, 'lon': -115.1537, 'name': 'McCarran International'},
        'PHX': {'lat': 33.4342, 'lon': -112.0116, 'name': 'Phoenix Sky Harbor'},
        'MIA': {'lat': 25.7959, 'lon': -80.2871, 'name': 'Miami International'},
        'SEA': {'lat': 47.4502, 'lon': -122.3088, 'name': 'Seattle-Tacoma International'}
    }
    
    # Airlines
    airlines = ['AA', 'DL', 'UA', 'WN', 'B6', 'AS', 'NK', 'F9', 'G4', 'SY']
    
    flights = []
    airport_codes = list(airports.keys())
    
    for i in range(count):
        # Random origin and destination
        origin = random.choice(airport_codes)
        destination = random.choice([code for code in airport_codes if code != origin])
        
        # Generate flight between airports with some movement
        origin_airport = airports[origin]
        dest_airport = airports[destination]
        
        # Add some variation to simulate flight path
        progress = random.uniform(0.1, 0.9)  # How far along the route
        
        lat = origin_airport['lat'] + (dest_airport['lat'] - origin_airport['lat']) * progress
        lon = origin_airport['lon'] + (dest_airport['lon'] - origin_airport['lon']) * progress
        
        # Add some random offset for realism
        lat += random.uniform(-0.5, 0.5)
        lon += random.uniform(-0.5, 0.5)
        
        flight = {
            'icao24': f'{random.randint(100000, 999999):06x}',
            'callsign': f'demo_{random.choice(airlines)}{random.randint(100, 9999)}',
            'origin_country': 'United States',
            'latitude': lat,
            'longitude': lon,
            'baro_altitude': random.randint(30000, 42000),
            'velocity': random.randint(200, 500),
            'true_track': random.randint(0, 360),
            'vertical_rate': random.randint(-500, 500),
            'last_position_update': int(time.time()),
            'on_ground': False,
            'source': 'Demo',
            'origin': origin,
            'destination': destination,
            'aircraft_type': random.choice(['B738', 'A320', 'B777', 'A321', 'E175'])
        }
        
        flights.append(flight)
    
    return {
        'flights': flights,
        'sources': ['Demo'],
        'timestamp': datetime.now().isoformat(),
        'count': len(flights)
    }

def get_demo_weather():
    """Generate demo weather data"""
    airports = ['JFK', 'LAX', 'ORD', 'ATL', 'DFW', 'DEN']
    weather_data = []
    
    for airport in airports:
        weather = {
            'station': airport,
            'temperature': random.randint(15, 35),
            'humidity': random.randint(30, 90),
            'pressure': random.randint(1010, 1030),
            'wind_speed': random.randint(5, 25),
            'wind_direction': random.randint(0, 360),
            'visibility': random.randint(5, 15),
            'conditions': random.choice(['Clear', 'Partly Cloudy', 'Overcast', 'Light Rain'])
        }
        weather_data.append(weather)
    
    return weather_data

if __name__ == "__main__":
    # Test the demo data generator
    print("🧪 Testing Demo Data Generator...")
    
    flights = generate_demo_flights(10)
    print(f"✅ Generated {len(flights['flights'])} demo flights")
    
    weather = get_demo_weather()
    print(f"✅ Generated {len(weather)} weather stations")
    
    print("\nSample flight:")
    if flights['flights']:
        flight = flights['flights'][0]
        print(f"  Callsign: {flight['callsign']}")
        print(f"  Route: {flight['origin']} → {flight['destination']}")
        print(f"  Position: {flight['latitude']:.2f}, {flight['longitude']:.2f}")
        print(f"  Altitude: {flight['baro_altitude']} ft")
    
    print("\n🎉 Demo data generator working correctly!")
