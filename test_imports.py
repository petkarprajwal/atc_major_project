#!/usr/bin/env python3
"""
Quick Import Test
Tests if all imports work correctly after fixes
"""

import sys
from pathlib import Path

# Add project directory to path
project_dir = Path(__file__).parent
sys.path.insert(0, str(project_dir))

def test_imports():
    """Test all critical imports"""
    print("🧪 Testing Fixed Imports...")
    print("-" * 40)
    
    try:
        print("✅ Testing utils.config...")
        from utils.config import Config
        config = Config()
        print("✅ Config - OK")
        
        print("✅ Testing models.collision_avoidance...")
        from models.collision_avoidance import CollisionAvoidanceModel
        model = CollisionAvoidanceModel()
        print("✅ CollisionAvoidanceModel - OK")
        
        print("✅ Testing models.runway_scheduler...")
        from models.runway_scheduler import RunwayScheduler, FlightType, Priority
        scheduler = RunwayScheduler()
        print("✅ RunwayScheduler - OK")
        
        print("✅ Testing utils.data_processing...")
        from utils.data_processing import FlightData, ConflictDetector
        print("✅ Data Processing - OK")
        
        print("-" * 40)
        print("🎉 ALL IMPORTS SUCCESSFUL!")
        print("✅ Dashboard should now launch without import errors")
        return True
        
    except Exception as e:
        print(f"❌ Import failed: {e}")
        print("-" * 40)
        print("⚠️  There are still import issues")
        return False

if __name__ == "__main__":
    success = test_imports()
    
    if success:
        print("\n🚀 Ready to launch dashboard:")
        print("   streamlit run dashboard/realtime_main.py")
        print("   or")
        print("   python launch_fixed.py")
    else:
        print("\n🔧 Import issues remain - using fallback demo mode")
        print("   Dashboard will still work with limited functionality")
