import React from 'react';
import { AlertCircle, RefreshCw } from 'lucide-react';

/**
 * ErrorMessage component - displays errors with retry option
 * @param {Object} props
 * @param {string} props.message - Error message
 * @param {Function} props.onRetry - Retry callback
 */
const ErrorMessage = ({ message, onRetry }) => {
  return (
    <div className="flex items-start gap-3 mb-4 animate-fade-in">
      <div className="flex-shrink-0 w-8 h-8 rounded-lg bg-red-500 dark:bg-red-600 flex items-center justify-center shadow-lg">
        <AlertCircle className="w-5 h-5 text-white" />
      </div>

      <div className="flex-1 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-2xl px-4 py-3 shadow-sm">
        <p className="text-sm text-red-800 dark:text-red-200 leading-relaxed">
          {message}
        </p>
        
        {onRetry && (
          <button
            onClick={onRetry}
            className="mt-2 inline-flex items-center gap-1.5 text-xs font-medium text-red-700 dark:text-red-300 hover:text-red-900 dark:hover:text-red-100 transition-colors"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            Try again
          </button>
        )}
      </div>
    </div>
  );
};

export default ErrorMessage;