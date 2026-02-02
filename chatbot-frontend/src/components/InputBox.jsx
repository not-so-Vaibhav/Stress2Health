import React, { useState } from 'react';
import { Send, Loader2 } from 'lucide-react';

/**
 * InputBox component - handles user input
 * @param {Object} props
 * @param {Function} props.onSend - Callback when message is sent
 * @param {boolean} props.disabled - Whether input is disabled
 * @param {boolean} props.isLoading - Whether bot is responding
 */
const InputBox = ({ onSend, disabled, isLoading }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const message = input.trim();
    if (!message || disabled) return;

    onSend(message);
    setInput('');
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(e);
    }
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="border-t border-gray-200 dark:border-gray-700 bg-white dark:bg-gray-800 px-4 py-4"
    >
      <div className="max-w-4xl mx-auto flex items-end gap-3">
        <div className="flex-1 relative">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={handleKeyDown}
            disabled={disabled}
            placeholder={
              disabled
                ? 'Waiting for response...'
                : 'Type your message here... (Press Enter to send, Shift+Enter for new line)'
            }
            rows={1}
            className="w-full resize-none rounded-xl border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-900 px-4 py-3 pr-12 text-gray-900 dark:text-gray-100 placeholder:text-gray-500 dark:placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-primary-500 dark:focus:ring-primary-400 focus:border-transparent transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed max-h-32 scrollbar-thin"
            style={{
              minHeight: '48px',
              maxHeight: '128px',
            }}
            onInput={(e) => {
              e.target.style.height = 'auto';
              e.target.style.height = Math.min(e.target.scrollHeight, 128) + 'px';
            }}
          />
          
          {/* Character count (optional) */}
          {input.length > 0 && (
            <div className="absolute bottom-1 right-12 text-xs text-gray-400 dark:text-gray-500">
              {input.length}
            </div>
          )}
        </div>

        <button
          type="submit"
          disabled={disabled || !input.trim()}
          className="flex-shrink-0 h-12 w-12 rounded-xl bg-gradient-to-br from-primary-500 to-primary-600 dark:from-primary-400 dark:to-primary-500 text-white flex items-center justify-center transition-all duration-200 hover:shadow-lg hover:scale-105 active:scale-95 disabled:opacity-50 disabled:cursor-not-allowed disabled:hover:scale-100 disabled:hover:shadow-none"
          aria-label="Send message"
        >
          {isLoading ? (
            <Loader2 className="w-5 h-5 animate-spin" />
          ) : (
            <Send className="w-5 h-5" />
          )}
        </button>
      </div>

      {/* Hint text */}
      <div className="max-w-4xl mx-auto mt-2 text-xs text-gray-500 dark:text-gray-400 text-center">
        Press <kbd className="px-1.5 py-0.5 bg-gray-200 dark:bg-gray-700 rounded">Enter</kbd> to send, 
        <kbd className="px-1.5 py-0.5 bg-gray-200 dark:bg-gray-700 rounded ml-1">Shift + Enter</kbd> for new line
      </div>
    </form>
  );
};

export default InputBox;