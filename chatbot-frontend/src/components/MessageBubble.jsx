import React from 'react';
import { Bot, User } from 'lucide-react';

/**
 * MessageBubble component - displays a single chat message
 * @param {Object} props
 * @param {Object} props.message - Message object { text, sender, timestamp }
 * @param {boolean} props.isBot - Whether message is from bot
 */
const MessageBubble = ({ message, isBot }) => {
  return (
    <div
      className={`flex items-start gap-3 mb-4 message-enter ${
        isBot ? 'justify-start' : 'justify-end'
      }`}
    >
      {isBot && (
        <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-gradient-to-br from-primary-500 to-primary-600 dark:from-primary-400 dark:to-primary-500 flex items-center justify-center shadow-lg">
          <Bot className="w-5 h-5 text-white" />
        </div>
      )}

      <div
        className={`max-w-[75%] md:max-w-[60%] ${
          isBot
            ? 'bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 border border-gray-200 dark:border-gray-700'
            : 'bg-gradient-to-br from-primary-500 to-primary-600 dark:from-primary-400 dark:to-primary-500 text-white'
        } rounded-2xl px-4 py-3 shadow-sm`}
      >
        <p className="text-[15px] leading-relaxed whitespace-pre-wrap break-words">
          {message.text}
        </p>
        <span
          className={`text-xs mt-1 block ${
            isBot
              ? 'text-gray-500 dark:text-gray-400'
              : 'text-primary-100 dark:text-primary-200'
          }`}
        >
          {message.timestamp}
        </span>
      </div>

      {!isBot && (
        <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-gradient-to-br from-gray-700 to-gray-800 dark:from-gray-600 dark:to-gray-700 flex items-center justify-center shadow-lg">
          <User className="w-5 h-5 text-white" />
        </div>
      )}
    </div>
  );
};

export default MessageBubble;