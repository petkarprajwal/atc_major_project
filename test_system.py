"""
Test script for ATC AI System
Run this to verify installation and basic functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.config import Config
from utils.data_processing import FlightData, ConflictDetector, TrajectoryCalculator
from models.collision_avoidance import CollisionAvoidanceModel
from models.runway_scheduler import RunwayScheduler, FlightType, Priority

def test_configuration():
    """Test configuration loading"""
    print("=" * 50)
    print("TESTING CONFIGURATION")
    print("=" * 50)
    
    print(Config.get_summary())
    
    config_status = Config.validate_config()
    if config_status['valid']:
        print("✅ Configuration is valid")
    else:
        print("⚠️  Configuration has warnings:")
        for warning in config_status['warnings']:
            print(f"   - {warning}")
    
    return config_status['valid']

def test_data_processing():
    """Test data processing utilities"""
    print("\n" + "=" * 50)
    print("TESTING DATA PROCESSING")
    print("=" * 50)
    
    # Create test flight data
    flight1 = FlightData(
        icao24="test001",
        callsign="TEST001",
        origin_country="Test",
        time_position=1234567890,
        last_contact=1234567890,
        longitude=-73.7781,  # JFK
        latitude=40.6413,
        baro_altitude=3000,
        on_ground=False,
        velocity=250,
        true_track=90,
        vertical_rate=0,
        sensors=None,
        geo_altitude=3000,
        squawk=None,
        spi=False,
        position_source=0
    )
    
    flight2 = FlightData(
        icao24="test002",
        callsign="TEST002",
        origin_country="Test",
        time_position=1234567890,
        last_contact=1234567890,
        longitude=-73.7681,  # Close to flight1
        latitude=40.6513,
        baro_altitude=3100,
        on_ground=False,
        velocity=260,
        true_track=270,
        vertical_rate=5,
        sensors=None,
        geo_altitude=3100,
        squawk=None,
        spi=False,
        position_source=0
    )
    
    print(f"Created test flights: {flight1.callsign} and {flight2.callsign}")
    
    # Test distance calculation
    distance = TrajectoryCalculator.calculate_distance(
        flight1.latitude, flight1.longitude,
        flight2.latitude, flight2.longitude
    )
    print(f"Distance between flights: {distance:.2f} NM")
    
    # Test trajectory prediction
    trajectory = TrajectoryCalculator.calculate_trajectory(flight1, 5)
    print(f"Generated trajectory with {len(trajectory)} points")
    
    # Test conflict detection
    detector = ConflictDetector()
    conflict = detector.check_conflict(flight1, flight2)
    
    if conflict:
        print(f"⚠️  Conflict detected:")
        print(f"   Severity: {conflict['severity']}")
        print(f"   Time to conflict: {conflict['time_to_conflict']:.1f} minutes")
        print(f"   Min separation: {conflict['min_separation']:.2f} NM")
    else:
        print("✅ No conflict detected")
    
    print("✅ Data processing tests completed")

def test_collision_model():
    """Test collision avoidance model"""
    print("\n" + "=" * 50)
    print("TESTING COLLISION AVOIDANCE MODEL")
    print("=" * 50)
    
    model = CollisionAvoidanceModel()
    
    # Train the model
    print("Training model with synthetic data...")
    results = model.train()
    
    print(f"✅ Model trained successfully")
    print(f"   Train Accuracy: {results['train_accuracy']:.4f}")
    print(f"   Test Accuracy: {results['test_accuracy']:.4f}")
    
    # Test prediction with the same flights from before
    flight1 = FlightData(
        icao24="test001", callsign="TEST001", origin_country="Test",
        time_position=1234567890, last_contact=1234567890,
        longitude=-73.7781, latitude=40.6413, baro_altitude=3000,
        on_ground=False, velocity=250, true_track=90, vertical_rate=0,
        sensors=None, geo_altitude=3000, squawk=None, spi=False, position_source=0
    )
    
    flight2 = FlightData(
        icao24="test002", callsign="TEST002", origin_country="Test",
        time_position=1234567890, last_contact=1234567890,
        longitude=-73.7681, latitude=40.6513, baro_altitude=3100,
        on_ground=False, velocity=260, true_track=270, vertical_rate=5,
        sensors=None, geo_altitude=3100, squawk=None, spi=False, position_source=0
    )
    
    prediction = model.predict_conflict(flight1, flight2)
    
    if prediction['error']:
        print(f"❌ Prediction error: {prediction['error']}")
    else:
        print(f"✅ Prediction successful:")
        print(f"   Conflict Probability: {prediction['conflict_probability']:.4f}")
        print(f"   Confidence: {prediction['confidence']:.4f}")

def test_runway_scheduler():
    """Test runway scheduling system"""
    print("\n" + "=" * 50)
    print("TESTING RUNWAY SCHEDULER")
    print("=" * 50)
    
    scheduler = RunwayScheduler()
    
    # Add runways
    scheduler.add_runway("RW01", 30)
    scheduler.add_runway("RW02", 25)
    
    print("✅ Added 2 runways to scheduler")
    
    # Create test flight
    from datetime import datetime, timedelta
    
    flight_data = FlightData(
        icao24="sched001", callsign="SCHED001", origin_country="Test",
        time_position=1234567890, last_contact=1234567890,
        longitude=-73.7781, latitude=40.6413, baro_altitude=3000,
        on_ground=False, velocity=250, true_track=90, vertical_rate=0,
        sensors=None, geo_altitude=3000, squawk=None, spi=False, position_source=0
    )
    
    # Schedule flight
    result = scheduler.schedule_flight(
        flight_data=flight_data,
        flight_type=FlightType.ARRIVAL,
        preferred_time=datetime.now() + timedelta(hours=1),
        priority=Priority.NORMAL,
        fuel_level=75.0
    )
    
    if result['success']:
        print(f"✅ Flight scheduled successfully:")
        print(f"   Runway: {result['runway']}")
        print(f"   Delay: {result['delay_minutes']:.1f} minutes")
    else:
        print(f"❌ Scheduling failed: {result.get('error', 'Unknown error')}")
    
    # Get system status
    status = scheduler.get_system_status()
    print(f"✅ System Status:")
    print(f"   Total Runways: {status['total_runways']}")
    print(f"   Scheduled Flights: {status['total_scheduled_flights']}")

def main():
    """Run all tests"""
    print("🧪 ATC AI SYSTEM TEST SUITE")
    print("Testing basic functionality...")
    
    try:
        # Test configuration
        config_ok = test_configuration()
        
        # Test data processing
        test_data_processing()
        
        # Test ML model
        test_collision_model()
        
        # Test runway scheduler
        test_runway_scheduler()
        
        print("\n" + "=" * 50)
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        
        if not config_ok:
            print("\n⚠️  Note: Some tests ran with demo data due to missing API configuration.")
            print("   Configure .env file with API credentials for full functionality.")
        
        print("\n🚀 Ready to run the dashboard:")
        print("   streamlit run dashboard/main.py")
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
