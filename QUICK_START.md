# 🚀 Quick Start Guide - AI Health Chatbot

## ✅ Final Ready Version

All errors have been resolved! The backend now runs on **port 5001** (to avoid macOS AirPlay Receiver conflict on port 5000).

---

## 📋 How to Start

### Step 1: Start the Backend

Open Terminal and run:

```bash
cd backend
python app.py
```

You should see:
```
🔄 Initializing AI Health Chatbot...
Model loaded from models/logistic
✅ Chatbot initialized successfully!
🚀 Backend running on http://localhost:5001
📝 Frontend should connect to: http://localhost:5001
```

### Step 2: Start the Frontend

Open a **NEW Terminal window** and run:

```bash
cd chatbot-frontend
npm run dev
```

The frontend will automatically open in your browser at `http://localhost:3000`

---

## 🎯 What's Fixed

✅ **Port Conflict Resolved**: Backend moved to port 5001  
✅ **Frontend API Updated**: Now connects to port 5001  
✅ **All Imports Fixed**: All modules properly imported  
✅ **Error Handling**: Comprehensive error handling added  
✅ **Input Validation**: All user inputs validated  
✅ **Session Management**: Proper conversation flow  

---

## 🔧 Troubleshooting

### Backend won't start?
- Make sure you're in the `backend` directory
- Check if port 5001 is available: `lsof -ti:5001`
- If port is in use, kill it: `lsof -ti:5001 | xargs kill`

### Frontend can't connect?
- Make sure backend is running first
- Check backend terminal for any error messages
- Verify backend is on port 5001 (check the startup message)

### Still having issues?
- Check both terminal windows for error messages
- Make sure all dependencies are installed:
  - Backend: `pip install -r requirements.txt`
  - Frontend: `cd chatbot-frontend && npm install`

---

## 📝 Port Configuration

- **Frontend**: `http://localhost:3000` (Vite dev server)
- **Backend**: `http://localhost:5001` (Flask API)

The frontend automatically connects to the backend on port 5001.

---

## ✨ You're All Set!

The application is ready to use. Start both servers and begin chatting with your AI Health Assistant!

