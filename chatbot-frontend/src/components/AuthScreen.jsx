/**
 * AuthScreen - Login and Signup forms using Supabase email+password auth
 * Simple, clean UI suitable for viva explanation
 */
import React, { useState } from 'react';
import { Activity, Mail, Lock, LogIn, UserPlus } from 'lucide-react';

export default function AuthScreen({ onSignIn, onSignUp, error, clearError }) {
  const [mode, setMode] = useState('login'); // 'login' | 'signup'
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [submitError, setSubmitError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    setSubmitError('');
    setSuccessMsg('');
    clearError?.();

    if (!email.trim() || !password) {
      setSubmitError('Please enter email and password.');
      return;
    }

    if (password.length < 6) {
      setSubmitError('Password must be at least 6 characters.');
      return;
    }

    try {
      if (mode === 'signup') {
        await onSignUp(email.trim(), password);
        setSuccessMsg('Account created! Check your email to confirm, or sign in below.');
        setMode('login');
        setPassword('');
      } else {
        await onSignIn(email.trim(), password);
      }
    } catch (err) {
      setSubmitError(err.message || 'Authentication failed.');
    }
  };

  const displayError = submitError || error;

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-b from-gray-50 to-gray-100 dark:from-gray-950 dark:to-gray-900 p-4">
      <div className="w-full max-w-md">
        {/* Logo & Title */}
        <div className="text-center mb-8">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-gradient-to-br from-primary-500 to-primary-600 mb-4">
            <Activity className="w-8 h-8 text-white" strokeWidth={2.5} />
          </div>
          <h1 className="text-2xl font-bold text-gray-900 dark:text-white">Stress2Health</h1>
          <p className="text-sm text-gray-500 dark:text-gray-400 mt-1">
            Sign in to save your health insights
          </p>
        </div>

        {/* Form Card */}
        <div className="bg-white dark:bg-gray-800 rounded-2xl shadow-lg border border-gray-200 dark:border-gray-700 p-6">
          <form onSubmit={handleSubmit} className="space-y-4">
            {displayError && (
              <div className="p-3 rounded-lg bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300 text-sm">
                {displayError}
              </div>
            )}
            {successMsg && (
              <div className="p-3 rounded-lg bg-green-50 dark:bg-green-900/20 text-green-700 dark:text-green-300 text-sm">
                {successMsg}
              </div>
            )}

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Email
              </label>
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  className="w-full pl-10 pr-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder:text-gray-500 focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  autoComplete="email"
                />
              </div>
            </div>

            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                Password
              </label>
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="••••••••"
                  className="w-full pl-10 pr-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-white placeholder:text-gray-500 focus:ring-2 focus:ring-primary-500 focus:border-transparent"
                  autoComplete={mode === 'signup' ? 'new-password' : 'current-password'}
                />
              </div>
              {mode === 'signup' && (
                <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                  Minimum 6 characters
                </p>
              )}
            </div>

            <button
              type="submit"
              className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-lg bg-primary-600 hover:bg-primary-700 text-white font-medium transition-colors"
            >
              {mode === 'login' ? (
                <>
                  <LogIn className="w-4 h-4" />
                  Sign In
                </>
              ) : (
                <>
                  <UserPlus className="w-4 h-4" />
                  Create Account
                </>
              )}
            </button>
          </form>

          <p className="mt-4 text-center text-sm text-gray-500 dark:text-gray-400">
            {mode === 'login' ? (
              <>
                Don&apos;t have an account?{' '}
                <button
                  type="button"
                  onClick={() => { setMode('signup'); setSubmitError(''); setSuccessMsg(''); }}
                  className="text-primary-600 hover:underline font-medium"
                >
                  Sign up
                </button>
              </>
            ) : (
              <>
                Already have an account?{' '}
                <button
                  type="button"
                  onClick={() => { setMode('login'); setSubmitError(''); }}
                  className="text-primary-600 hover:underline font-medium"
                >
                  Sign in
                </button>
              </>
            )}
          </p>
        </div>

        <p className="text-center text-xs text-gray-400 dark:text-gray-500 mt-6">
          Educational project • Your data is stored securely in Supabase
        </p>
      </div>
    </div>
  );
}
