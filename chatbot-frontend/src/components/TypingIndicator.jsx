import React from 'react';
import { Bot } from 'lucide-react';

/**
 * TypingIndicator - Shows when bot is typing
 */
const TypingIndicator = () => {
  return (
    <div className="flex items-start gap-3 mb-4 animate-fade-in">
      <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-gradient-to-br from-primary-500 to-primary-600 dark:from-primary-400 dark:to-primary-500 flex items-center justify-center shadow-lg">
        <Bot className="w-5 h-5 text-white" />
      </div>

      <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-2xl px-4 py-3 shadow-sm">
        <div className="flex items-center gap-1">
          <div className="typing-dot w-2 h-2 bg-gray-400 dark:bg-gray-500 rounded-full"></div>
          <div className="typing-dot w-2 h-2 bg-gray-400 dark:bg-gray-500 rounded-full"></div>
          <div className="typing-dot w-2 h-2 bg-gray-400 dark:bg-gray-500 rounded-full"></div>
        </div>
      </div>
    </div>
  );
};

export default TypingIndicator;