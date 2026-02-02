# How to Start the Frontend

## Quick Start

1. **Open Terminal and navigate to the frontend directory:**
   ```bash
   cd chatbot-frontend
   ```

2. **Start the development server:**
   ```bash
   npm run dev
   ```

3. **Access the frontend in your browser:**
   - The server will automatically open your browser
   - OR manually go to: **http://localhost:3000** or **http://127.0.0.1:3000**
   
   ⚠️ **IMPORTANT:** Make sure to include `:3000` in the URL!

## Start Backend (Required for Chat to Work)

In a **separate terminal window:**

```bash
cd backend
python app.py
```

The backend will run on http://localhost:5000

## Troubleshooting

- **Blank white page?** Make sure you're accessing `http://localhost:3000` (with port 3000)
- **Can't connect to backend?** Make sure the backend is running on port 5000
- **Port already in use?** Kill the process: `lsof -ti:3000 | xargs kill` (Mac/Linux)

