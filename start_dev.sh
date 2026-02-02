#!/bin/bash

# Start Frontend and Backend Development Servers

echo "🚀 Starting AI Health Chatbot Development Servers..."
echo ""

# Check if backend is already running
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Backend already running on port 5000"
else
    echo "📦 Starting Backend on http://localhost:5000..."
    cd backend
    python app.py &
    BACKEND_PID=$!
    cd ..
    echo "✅ Backend started (PID: $BACKEND_PID)"
fi

# Wait a moment for backend to start
sleep 2

# Check if frontend is already running
if lsof -Pi :3000 -sTCP:LISTEN -t >/dev/null ; then
    echo "⚠️  Frontend already running on port 3000"
else
    echo "🎨 Starting Frontend on http://localhost:3000..."
    cd chatbot-frontend
    npm run dev &
    FRONTEND_PID=$!
    cd ..
    echo "✅ Frontend started (PID: $FRONTEND_PID)"
fi

echo ""
echo "=========================================="
echo "✅ Servers are starting!"
echo ""
echo "📍 Frontend: http://localhost:3000"
echo "📍 Backend:  http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop all servers"
echo "=========================================="

# Wait for user interrupt
wait

