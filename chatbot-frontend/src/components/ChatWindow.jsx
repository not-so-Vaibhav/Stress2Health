import React, { useEffect, useRef } from 'react';
import MessageBubble from './MessageBubble';
import TypingIndicator from './TypingIndicator';
import ErrorMessage from './ErrorMessage';
import WelcomeScreen from './WelcomeScreen';

/**
 * ChatWindow component - displays all messages with auto-scroll
 * @param {Object} props
 * @param {Array} props.messages - Array of message objects
 * @param {boolean} props.isTyping - Whether bot is typing
 * @param {string} props.error - Error message if any
 * @param {Function} props.onRetry - Retry callback for errors
 */
const ChatWindow = ({ messages, isTyping, error, onRetry }) => {
  const messagesEndRef = useRef(null);
  const chatContainerRef = useRef(null);

  // Auto-scroll to bottom when new messages arrive
  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ 
        behavior: 'smooth',
        block: 'end'
      });
    }
  }, [messages, isTyping, error]);

  return (
    <div
      ref={chatContainerRef}
      className="flex-1 overflow-y-auto scrollbar-thin px-4 py-6"
    >
      <div className="max-w-4xl mx-auto">
        {/* Show welcome screen when no messages */}
        {messages.length === 0 && !isTyping && !error && (
          <WelcomeScreen />
        )}

        {/* Messages */}
        {messages.map((message, index) => (
          <MessageBubble
            key={index}
            message={message}
            isBot={message.sender === 'bot'}
          />
        ))}

        {/* Typing Indicator */}
        {isTyping && <TypingIndicator />}

        {/* Error Message */}
        {error && <ErrorMessage message={error} onRetry={onRetry} />}

        {/* Scroll anchor */}
        <div ref={messagesEndRef} />
      </div>
    </div>
  );
};

export default ChatWindow;