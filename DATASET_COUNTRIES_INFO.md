# Country Datasets and Data Sources - ATC AI System

## 📍 Geographic Coverage Overview

Your Real-time ATC AI System uses flight data from **multiple countries and regions worldwide**. Here's a comprehensive breakdown:

## 🌍 Primary Data Sources and Coverage

### 1. **OpenSky Network API** 
- **Global Coverage**: Worldwide flight tracking
- **Primary Countries**: All countries with ADS-B coverage
- **Major Regions**: 
  - North America (USA, Canada, Mexico)
  - Europe (UK, France, Germany, Netherlands, etc.)
  - Asia-Pacific (Japan, Australia, Singapore, etc.)
  - Middle East, South America, Africa (partial coverage)

### 2. **AviationStack API**
- **Coverage**: Global commercial flights
- **Strong Coverage**: 
  - United States
  - European Union countries
  - Major Asia-Pacific hubs
  - International routes

### 3. **FlightAware AeroAPI**
- **Coverage**: Global with emphasis on:
  - United States (comprehensive)
  - Canada
  - Europe
  - Major international airports worldwide

### 4. **RapidAPI (AeroDataBox)**
- **Coverage**: Global aircraft and flight data
- **Specializes in**: International commercial aviation

## 🏢 Major Airports by Country (Configured in System)

### **United States**
- JFK - John F. Kennedy International Airport (New York)
- LAX - Los Angeles International Airport (California) 
- ORD - Chicago O'Hare International Airport (Illinois)
- DFW - Dallas/Fort Worth International Airport (Texas)
- DEN - Denver International Airport (Colorado)

### **United Kingdom**
- LHR - London Heathrow Airport

### **France** 
- CDG - Charles de Gaulle Airport (Paris)

### **Japan**
- NRT - Narita International Airport (Tokyo)

### **Australia**
- SYD - Sydney Kingsford Smith Airport

### **Singapore**
- SIN - Singapore Changi Airport

## 📊 Demo Data Configuration

When APIs are unavailable, the system generates demo data primarily using:

### **Primary Demo Country**: United States
- **Origin/Destination Airports**: JFK, LAX, ORD, ATL, DFW, DEN, LAS, PHX
- **Airlines**: AA (American), DL (Delta), UA (United), WN (Southwest), B6 (JetBlue), AS (Alaska)
- **Flight Paths**: Realistic routes between major US airports
- **Coordinates**: Accurate latitude/longitude for US airspace

### **Flight Characteristics in Demo Data**:
- **Altitudes**: 30,000 - 42,000 feet (typical commercial cruise)
- **Velocities**: 200 - 500 knots (realistic commercial speeds)
- **Countries**: All demo flights flagged as "United States" origin

## 🌐 Real-Time Data Geographic Scope

### **Live Data Collection Covers**:
1. **North America**: USA, Canada, Mexico
2. **Europe**: UK, France, Germany, Netherlands, Spain, Italy, Scandinavia
3. **Asia-Pacific**: Japan, Australia, Singapore, Hong Kong, South Korea
4. **Middle East**: UAE, Qatar, Saudi Arabia (major hubs)
5. **Other Regions**: Limited coverage in South America, Africa

### **Bounding Box Configurations**:
- **Default Global**: No geographic restrictions
- **Regional Focus**: Can be configured for specific continents
- **Airport-Centric**: 50km radius around major international hubs

## 📡 Data Source Priority and Fallback

### **Primary Source Hierarchy**:
1. **OpenSky Network** (Free, global, real-time ADS-B data)
2. **AviationStack** (Commercial, global flight schedules)
3. **FlightAware** (Premium, comprehensive US + international)
4. **RapidAPI** (Alternative commercial source)
5. **Demo Data** (US-focused realistic simulation)

## 🎯 Country-Specific Features

### **Enhanced Coverage Countries**:
- **United States**: Complete ADS-B coverage, multiple API sources
- **European Union**: Excellent coverage through OpenSky and commercial APIs
- **Major Aviation Hubs**: Comprehensive data for international airports

### **Weather Data Integration**:
- **Global**: OpenWeatherMap API covers all countries
- **Major Airports**: Real-time weather for primary hubs worldwide
- **Demo Weather**: US major cities (NYC, LA, Chicago, Atlanta, Dallas, Denver)

## 🔧 System Configuration for Different Regions

### **To Focus on Specific Countries**:
1. Modify `MAJOR_AIRPORTS` in `utils/api_client.py`
2. Update demo data airports in `dashboard/realtime_main.py`
3. Configure API bounding boxes for regional focus
4. Set weather monitoring locations

### **Current Default Settings**:
- **Primary Focus**: United States domestic flights
- **Secondary Coverage**: Major international routes
- **Global Capability**: All countries with ADS-B transponders

## 📈 Data Volume by Region

### **Typical Flight Counts** (in demo/test mode):
- **US Domestic**: 12+ simultaneous flights
- **International**: Variable based on API availability
- **Global Real-time**: 50-100+ flights depending on API keys

### **Coverage Quality**:
- **Excellent**: USA, Europe, Australia, Japan
- **Good**: Canada, major Asian hubs, Middle East hubs
- **Limited**: South America, Africa (except major airports)

## 🚀 Expanding Geographic Coverage

### **To Add New Countries**:
1. Add airports to `MAJOR_AIRPORTS` dictionary
2. Include country-specific airlines in demo data
3. Configure weather monitoring for new regions
4. Update bounding boxes for API queries

### **Current Expandability**:
- ✅ Any country with ICAO airport codes
- ✅ Any region covered by OpenSky Network
- ✅ All countries supported by weather APIs
- ✅ Customizable demo data for any nation

---

## 🎉 Summary

Your ATC AI System is designed with **global capability** but currently optimized for:

### **Primary Coverage**: 
- 🇺🇸 **United States** (comprehensive)
- 🇬🇧 **United Kingdom** (major airports)  
- 🇫🇷 **France** (major airports)
- 🇯🇵 **Japan** (major airports)
- 🇦🇺 **Australia** (major airports)
- 🇸🇬 **Singapore** (major airports)

### **Data Sources**: 
- **Real-time**: Global coverage through multiple aviation APIs
- **Demo Mode**: US-focused realistic flight simulation
- **Weather**: Worldwide coverage
- **Expandable**: Easy to add any country or region

The system automatically falls back to demo data (US-focused) when APIs are unavailable, ensuring continuous operation regardless of API connectivity.
