chatbot-frontend/
├── src/
│   ├── components/          # React components
│   │   ├── Header.jsx       # App header with theme toggle
│   │   ├── ChatWindow.jsx   # Main chat container
│   │   ├── MessageBubble.jsx # Individual message component
│   │   ├── InputBox.jsx     # Message input with send button
│   │   ├── TypingIndicator.jsx # Animated typing dots
│   │   ├── ErrorMessage.jsx # Error display with retry
│   │   └── WelcomeScreen.jsx # Initial welcome screen
│   ├── context/
│   │   └── ThemeContext.jsx # Dark mode state management
│   ├── services/
│   │   └── api.js           # Backend API integration
│   ├── App.jsx              # Main app component
│   ├── main.jsx             # React entry point
│   └── index.css            # Global styles + Tailwind
├── index.html               # HTML template
├── vite.config.js           # Vite configuration
├── tailwind.config.js       # Tailwind CSS config
├── postcss.config.js        # PostCSS config
├── package.json             # Dependencies
├── .env.example             # Environment template
└── README.md                # This file