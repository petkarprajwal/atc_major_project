# 🚀 ATC AI System - Quick Start Guide

## 📋 Project Overview

This is a comprehensive **AI-powered Air Traffic Control System** that implements:

✅ **Predictive Collision Avoidance** - ML-based conflict detection  
✅ **Real-Time Runway Scheduling** - Optimized runway management  
✅ **Weather-Aware Route Planning** - Weather integration and hazard detection  
✅ **Interactive Dashboard** - Streamlit-based web interface  

## 🎯 Key Features

### 🛡️ Collision Avoidance
- Random Forest ML model for conflict prediction
- Physics-based trajectory calculations
- Real-time conflict detection and alerts
- 5-10 minute prediction horizon

### 🛬 Runway Management
- Priority-based scheduling system
- Dynamic capacity optimization
- Emergency flight handling
- Delay minimization algorithms

### 🌤️ Weather Integration
- Live weather data from OpenWeatherMap
- Automated hazard detection
- Weather-aware routing (planned)
- Impact assessment tools

### 📊 Dashboard
- Real-time flight tracking
- Interactive visualizations
- Multi-module navigation
- Live data updates

## 🚀 Quick Setup

### Option 1: Automatic Setup (Recommended)

**Windows:**
```bash
# Double-click setup.bat or run in PowerShell:
.\setup.bat
```

**Mac/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install packages
pip install -r requirements.txt

# 4. Test system
python test_system.py

# 5. Run dashboard
streamlit run dashboard/main.py
```

## 🔧 Configuration (Optional)

For live data, create `.env` file:

```env
OPENSKY_USERNAME=your_username
OPENSKY_PASSWORD=your_password
OPENWEATHER_API_KEY=your_api_key
```

**Get API Access:**
- OpenSky Network: [opensky-network.org](https://opensky-network.org) (free)
- OpenWeatherMap: [openweathermap.org/api](https://openweathermap.org/api) (free)

## 🎮 Usage

### 1. Start the Dashboard
```bash
streamlit run dashboard/main.py
```

### 2. Open Browser
Navigate to: `http://localhost:8501`

### 3. Explore Modules
- **📊 Main Dashboard** - System overview
- **🛡️ Collision Avoidance** - Train ML model and detect conflicts
- **🛬 Runway Management** - Schedule flights and manage runways  
- **🌤️ Weather Integration** - Monitor weather conditions

## 🧪 Demo Mode

The system works fully in **demo mode** without API credentials:
- Synthetic flight data generation
- All AI algorithms functional
- Complete dashboard experience
- Perfect for testing and learning

## 📖 Documentation

- **User Manual**: `documentation/user_manual.md`
- **Technical Docs**: `documentation/technical_docs.md`
- **API Reference**: See individual module docstrings

## 🛠️ Development

### Run Tests
```bash
python test_system.py          # Full system test
python -m pytest tests/        # Unit tests
python -m pytest tests/test_unit.py -v  # Verbose unit tests
```

### Code Structure
```
atc_ai_project/
├── utils/           # Core utilities and data processing
├── models/          # Machine learning models
├── dashboard/       # Streamlit web interface
├── tests/           # Test suites
└── documentation/   # Project documentation
```

## 🎯 Success Metrics

- **Prediction Accuracy**: >85% for collision detection
- **Response Time**: <2 seconds for conflict alerts
- **System Uptime**: 95%+ during operations
- **User Experience**: Intuitive dashboard interface

## 🔍 Troubleshooting

### Common Issues

**"Import errors"**
```bash
pip install -r requirements.txt
```

**"No flights detected"**
- Check internet connection
- Wait for API rate limits to reset
- Use demo mode (no configuration needed)

**"Port already in use"**
```bash
streamlit run dashboard/main.py --server.port 8502
```

### Performance Tips
- Select specific airports vs. global monitoring
- Use auto-refresh sparingly
- Close unused browser tabs

## 📊 System Requirements

**Minimum:**
- Python 3.8+
- 4GB RAM
- 1GB storage

**Recommended:**
- Python 3.9+
- 8GB RAM
- Broadband internet (for live data)

## 🎓 Educational Use

This system is perfect for:
- **Learning AI/ML applications** in aviation
- **Understanding air traffic control** systems
- **Exploring real-time data processing**
- **Demonstrating safety-critical algorithms**

## ⚠️ Important Notice

This is an **educational and demonstration system**. It should **NOT** be used for actual air traffic control operations. Real ATC systems require certification, extensive testing, and regulatory approval.

## 🤝 Contributing

The project is designed for educational purposes and demonstrations. Feel free to:
- Extend the ML models
- Add new visualization features
- Integrate additional data sources
- Improve the algorithms

## 📞 Support

For questions or issues:
1. Check the documentation
2. Review error messages in the dashboard sidebar
3. Try the troubleshooting steps above
4. Restart the application

## 🌟 Next Steps

After setup:
1. **Explore the dashboard** - Try all four modules
2. **Train the ML model** - Go to Collision Avoidance module
3. **Schedule some flights** - Use the Runway Management module
4. **Check weather data** - Configure APIs for live weather
5. **Read the documentation** - Learn about the algorithms

---

## 🎉 You're Ready!

The ATC AI System is now ready to use. Start with:

```bash
streamlit run dashboard/main.py
```

Then open your browser to `http://localhost:8501` and explore the future of AI-powered air traffic control!

**Happy flying! ✈️**
