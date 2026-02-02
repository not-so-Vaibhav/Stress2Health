import React from 'react';
import { Moon, Sun, Activity, MessageSquarePlus, LogOut, History } from 'lucide-react';
import { useTheme } from '../context/ThemeContext';

const Header = ({ userName, userEmail, onEditProfile, onNewChat, onSignOut, onShowHistory }) => {
  const { theme, toggleTheme } = useTheme();

  const displayName = userName?.trim() || userEmail?.split('@')[0] || 'Guest';

  return (
    <header className="border-b border-gray-200 dark:border-gray-800 bg-white/90 dark:bg-gray-900/80 sticky top-0 z-10 backdrop-blur-sm">
      <div className="max-w-7xl mx-auto px-4 py-4 flex items-center justify-between">
        {/* Logo and Title */}
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-primary-500 to-primary-600 dark:from-primary-400 dark:to-primary-500 flex items-center justify-center shadow-lg">
            <Activity className="w-6 h-6 text-white" strokeWidth={2.5} />
          </div>
          <div>
            <h1 className="text-xl md:text-2xl font-display font-bold text-gray-900 dark:text-white">
              Stress2Health
            </h1>
            <p className="text-xs text-gray-600 dark:text-gray-400 font-medium">
              Personal stress & lifestyle insights
            </p>
          </div>
        </div>

        <div className="flex items-center gap-2 sm:gap-3">
          <button
            type="button"
            onClick={onNewChat}
            className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-gray-900 dark:hover:text-gray-200 transition-colors"
            title="Start new chat"
          >
            <MessageSquarePlus className="w-4 h-4" />
            <span className="hidden sm:inline">New chat</span>
          </button>
          {onShowHistory && (
            <button
              type="button"
              onClick={onShowHistory}
              className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium text-gray-600 dark:text-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800 hover:text-gray-900 dark:hover:text-gray-200 transition-colors"
              title="View health history"
            >
              <History className="w-4 h-4" />
              <span className="hidden sm:inline">History</span>
            </button>
          )}
          <button
            type="button"
            onClick={onEditProfile}
            className="hidden sm:flex items-center gap-2 px-3 py-1.5 rounded-full border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-800 text-xs text-gray-700 dark:text-gray-200 hover:bg-gray-100 dark:hover:bg-gray-700 transition-colors"
          >
            <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-primary-500 text-white text-xs font-medium">
              {displayName.charAt(0).toUpperCase()}
            </span>
            <span className="font-medium truncate max-w-[120px]">
              {displayName}
            </span>
          </button>

          {onSignOut && (
            <button
              type="button"
              onClick={onSignOut}
              className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-lg text-xs font-medium text-gray-600 dark:text-gray-400 hover:bg-red-50 dark:hover:bg-red-900/20 hover:text-red-600 dark:hover:text-red-400 transition-colors"
              title="Sign out"
            >
              <LogOut className="w-4 h-4" />
              <span className="hidden sm:inline">Sign out</span>
            </button>
          )}

          {/* Theme Toggle */}
          <button
            onClick={toggleTheme}
            className="w-10 h-10 rounded-lg bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 flex items-center justify-center transition-all duration-200 hover:scale-105 active:scale-95"
            aria-label="Toggle theme"
          >
            {theme === 'light' ? (
              <Moon className="w-5 h-5 text-gray-700 dark:text-gray-200" />
            ) : (
              <Sun className="w-5 h-5 text-gray-200" />
            )}
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;