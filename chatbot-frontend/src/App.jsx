import React, { useState, useCallback, useEffect } from "react";
import Header from "./components/Header";
import ChatWindow from "./components/ChatWindow";
import InputBox from "./components/InputBox";
import AuthScreen from "./components/AuthScreen";
import HealthHistory from "./components/HealthHistory";
import { sendMessage, getStoredChat, saveChat, clearStoredChat } from "./services/api";
import { saveHealthData } from "./services/supabaseHealth";
import { useAuth } from "./context/AuthContext";
import { supabase } from "./lib/supabase";

function getTime() {
  return new Date().toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
  });
}

function App() {
  const { user, loading: authLoading, signIn, signUp, signOut } = useAuth();
  const [authError, setAuthError] = useState("");
  const [showHistory, setShowHistory] = useState(false);

  // When Supabase is configured, require auth. Otherwise allow guest.
  const requiresAuth = !!supabase;
  const showAuth = requiresAuth && !authLoading && !user;

  const [messages, setMessages] = useState([
    {
      text: "Welcome to Stress2Health 👋\nI'm your AI assistant. Tell me a bit about how you're feeling today.",
      sender: "bot",
      timestamp: getTime(),
    },
  ]);
  const [sessionId, setSessionId] = useState(null);
  const [isTyping, setIsTyping] = useState(false);
  const [error, setError] = useState(null);
  const [lastUserMessage, setLastUserMessage] = useState(null);
  const [userName, setUserName] = useState(() => {
    try {
      return localStorage.getItem("stress2health_userName") || "";
    } catch {
      return "";
    }
  });

  useEffect(() => {
    const stored = getStoredChat();
    if (stored?.messages?.length) {
      setMessages(stored.messages);
      setSessionId(stored.sessionId ?? null);
    }
  }, []);

  useEffect(() => {
    if (messages.length && (messages.length > 1 || sessionId)) {
      saveChat(messages, sessionId);
    }
  }, [messages, sessionId]);

  useEffect(() => {
    try {
      if (userName) localStorage.setItem("stress2health_userName", userName);
    } catch {}
  }, [userName]);

  const handleEditProfile = useCallback(() => {
    const name = window.prompt("How should I address you?", userName || "");
    if (name && name.trim().length > 0) {
      setUserName(name.trim());
    }
  }, [userName]);

  const handleNewChat = useCallback(() => {
    clearStoredChat();
    setMessages([
      {
        text: "Welcome to Stress2Health 👋\nI'm your AI assistant. Tell me a bit about how you're feeling today.",
        sender: "bot",
        timestamp: getTime(),
      },
    ]);
    setSessionId(null);
    setError(null);
    setLastUserMessage(null);
  }, []);

  const handleSendMessage = useCallback(async (text) => {
    if (!text.trim()) return;

    setError(null);

    const userMsg = {
      text,
      sender: "user",
      timestamp: getTime(),
    };

    setMessages((prev) => [...prev, userMsg]);
    setLastUserMessage(text);
    setIsTyping(true);

    try {
      const { reply, sessionId: newSessionId, healthData } = await sendMessage(text, sessionId);

      const botMsg = {
        text: reply || "I’m analyzing your stress and lifestyle patterns…",
        sender: "bot",
        timestamp: getTime(),
      };

      setMessages((prev) => [...prev, botMsg]);
      setSessionId(newSessionId);
      if (healthData && user) {
        const { error: saveErr } = await saveHealthData(healthData, user.id);
        if (saveErr) console.warn("Failed to save health data:", saveErr);
      }
    } catch (err) {
      setError(err.message || "Unable to connect to AI service.");
    } finally {
      setIsTyping(false);
    }
  }, [sessionId, user]);

  const handleRetry = useCallback(() => {
    if (lastUserMessage) {
      setError(null);
      handleSendMessage(lastUserMessage);
    }
  }, [lastUserMessage, handleSendMessage]);

  const handleSignIn = async (email, password) => {
    setAuthError("");
    try {
      await signIn(email, password);
    } catch (err) {
      setAuthError(err.message || "Sign in failed.");
    }
  };

  const handleSignUp = async (email, password) => {
    setAuthError("");
    try {
      await signUp(email, password);
    } catch (err) {
      setAuthError(err.message || "Sign up failed.");
    }
  };

  // Auth screen when Supabase configured and not logged in
  if (showAuth) {
    return (
      <AuthScreen
        onSignIn={handleSignIn}
        onSignUp={handleSignUp}
        error={authError}
        clearError={() => setAuthError("")}
      />
    );
  }

  // Loading auth state
  if (requiresAuth && authLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
        <p className="text-gray-500 dark:text-gray-400">Loading...</p>
      </div>
    );
  }

  return (
    <div className="h-screen flex flex-col bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-950 dark:to-gray-900">
      {/* Header */}
      <Header
          userName={userName}
          userEmail={user?.email}
          onEditProfile={handleEditProfile}
          onNewChat={handleNewChat}
          onSignOut={user ? signOut : undefined}
          onShowHistory={user ? () => setShowHistory(true) : undefined}
        />

      {/* Chat Area */}
      <ChatWindow
        messages={messages}
        isTyping={isTyping}
        error={error}
        onRetry={handleRetry}
      />

      {/* Input */}
      <InputBox
        onSend={handleSendMessage}
        disabled={isTyping}
        isLoading={isTyping}
      />

      {showHistory && <HealthHistory onClose={() => setShowHistory(false)} />}

      {/* Footer */}
      <footer className="border-t border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 py-2">
        <p className="text-xs text-center text-gray-500 dark:text-gray-400">
          Educational purpose only • Not a medical diagnosis
        </p>
      </footer>
    </div>
  );
}

export default App;
