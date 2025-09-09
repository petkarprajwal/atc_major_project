# 🚀 **MANUAL LAUNCH GUIDE - ENHANCED ATC DASHBOARD**

## ⚠️ **Connection Refused? Follow These Steps:**

### **🔥 QUICK FIX - 3 Simple Steps:**

#### **Step 1: Open Command Prompt**
- Press `Windows + R`
- Type `cmd` and press Enter
- Or open PowerShell

#### **Step 2: Navigate to Project**
```bash
cd "c:\Users\Petka\Desktop\ATC\atc_ai_project"
```

#### **Step 3: Launch Dashboard**
```bash
streamlit run dashboard/realtime_main.py
```

### **🌐 EXPECTED OUTPUT:**
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

### **🎯 ACCESS DASHBOARD:**
- **Click the Local URL** that appears in terminal
- **Or manually open**: `http://localhost:8501` in your browser

---

## 🔧 **TROUBLESHOOTING CONNECTION ISSUES:**

### **Issue 1: "Connection Refused"**
**Cause**: Streamlit server isn't running
**Solution**: Make sure you see the "Local URL" message in terminal

### **Issue 2: "Port Already in Use"**
**Cause**: Another app is using port 8501
**Solution**: Use different port
```bash
streamlit run dashboard/realtime_main.py --server.port 8502
```
Then visit: `http://localhost:8502`

### **Issue 3: "Command Not Found"**
**Cause**: Streamlit not installed
**Solution**: Install Streamlit
```bash
pip install streamlit
```

### **Issue 4: Browser Won't Open**
**Cause**: Firewall or antivirus blocking
**Solutions**:
- **Disable firewall temporarily**
- **Add Python/Streamlit to antivirus exceptions**
- **Try different browser** (Chrome, Edge, Firefox)

### **Issue 5: "Module Not Found"**
**Cause**: Missing dependencies
**Solution**: Install all requirements
```bash
pip install -r requirements.txt
```

---

## 🎮 **ALTERNATIVE LAUNCH METHODS:**

### **Method 1: Double-click Batch File**
```bash
# Double-click this file:
start_dashboard.bat
```

### **Method 2: Python Launcher**
```bash
python start_now.py
```

### **Method 3: Manual Command**
```bash
python -m streamlit run dashboard/realtime_main.py
```

### **Method 4: Different Port**
```bash
streamlit run dashboard/realtime_main.py --server.port 8080
```
Then visit: `http://localhost:8080`

---

## 🌐 **WHAT YOU SHOULD SEE:**

### **In Terminal:**
```
Collecting usage statistics...
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.1.100:8501
```

### **In Browser:**
- **🎯 Enhanced Real-time ATC Dashboard**
- **⚡ Real-time Controls Panel**
- **🗺️ Live Flight Map**
- **📊 Performance Metrics**
- **🔔 Alert System**

---

## 🆘 **STILL NOT WORKING?**

### **Check These:**

1. **Python Installation**
   ```bash
   python --version
   ```
   Should show Python 3.8+

2. **Streamlit Installation**
   ```bash
   streamlit --version
   ```
   Should show Streamlit version

3. **Project Directory**
   ```bash
   dir dashboard
   ```
   Should show `realtime_main.py`

4. **Dependencies**
   ```bash
   python test_enhanced_system.py
   ```
   Should show all tests passing

### **Emergency Fallback:**
If nothing works, try the **standard dashboard**:
```bash
streamlit run dashboard/main.py
```

---

## 🎉 **ONCE IT'S WORKING:**

### **🚀 Features to Try:**
1. **Click "Start Real-time"** - Begin live data streaming
2. **Explore Flight Map** - See aircraft in real-time
3. **Check Collision Detection** - AI-powered conflict alerts
4. **Monitor Performance** - System health metrics
5. **Test WebSocket** - Live browser updates

### **🔧 Configuration:**
- **Demo Mode**: Works immediately (no setup needed)
- **Live APIs**: Create `.env` file with your API keys
- **Real-time**: 2-second updates with WebSocket streaming

---

## 📞 **NEED HELP?**

### **Common Issues & Solutions:**

| Issue | Solution |
|-------|----------|
| Connection refused | Start Streamlit server first |
| Port in use | Use `--server.port 8502` |
| Module not found | Run `pip install streamlit` |
| Browser won't open | Check firewall/antivirus |
| Slow loading | Try different browser |

### **Quick Diagnostic:**
```bash
# Test if everything is working:
python test_enhanced_system.py

# Check port availability:
netstat -an | findstr 8501
```

---

**🎯 The key is seeing "Local URL: http://localhost:8501" in your terminal!**

**Once you see that message, click the URL or copy it to your browser! 🚀**
