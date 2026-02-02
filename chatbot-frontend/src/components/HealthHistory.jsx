/**
 * HealthHistory - View past health assessments from Supabase
 * Fetches user_health_data (RLS ensures only own records)
 */
import React, { useEffect, useState } from 'react';
import { X, Activity, Calendar } from 'lucide-react';
import { fetchHealthHistory } from '../services/supabaseHealth';

export default function HealthHistory({ onClose }) {
  const [records, setRecords] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function load() {
      setLoading(true);
      setError(null);
      const { data, error: err } = await fetchHealthHistory();
      setRecords(data ?? []);
      setError(err?.message ?? null);
      setLoading(false);
    }
    load();
  }, []);

  const formatDate = (ts) => {
    if (!ts) return '';
    const d = new Date(ts);
    return d.toLocaleDateString() + ' ' + d.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50" onClick={onClose}>
      <div
        className="bg-white dark:bg-gray-800 rounded-2xl shadow-xl max-w-2xl w-full max-h-[80vh] overflow-hidden flex flex-col"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="flex items-center justify-between p-4 border-b border-gray-200 dark:border-gray-700">
          <h2 className="text-lg font-semibold text-gray-900 dark:text-white flex items-center gap-2">
            <Activity className="w-5 h-5 text-primary-500" />
            Your Health History
          </h2>
          <button
            onClick={onClose}
            className="p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 text-gray-500"
            aria-label="Close"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="flex-1 overflow-y-auto p-4">
          {loading && (
            <p className="text-center text-gray-500 dark:text-gray-400 py-8">Loading...</p>
          )}
          {error && (
            <div className="p-4 rounded-lg bg-red-50 dark:bg-red-900/20 text-red-700 dark:text-red-300 text-sm">
              {error}
            </div>
          )}
          {!loading && !error && records.length === 0 && (
            <p className="text-center text-gray-500 dark:text-gray-400 py-8">
              No records yet. Complete an assessment to save your first result.
            </p>
          )}
          {!loading && records.length > 0 && (
            <div className="space-y-4">
              {records.map((r) => (
                <div
                  key={r.id}
                  className="p-4 rounded-xl border border-gray-200 dark:border-gray-700 bg-gray-50 dark:bg-gray-900/50"
                >
                  <div className="flex items-center gap-2 text-xs text-gray-500 dark:text-gray-400 mb-3">
                    <Calendar className="w-4 h-4" />
                    {formatDate(r.created_at)}
                  </div>
                  <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-sm mb-2">
                    <span className="font-medium text-gray-700 dark:text-gray-300">Stress</span>
                    <span className="capitalize">{r.stress_level}</span>
                    <span className="font-medium text-gray-700 dark:text-gray-300">Sleep</span>
                    <span>{r.sleep_hours}h</span>
                    <span className="font-medium text-gray-700 dark:text-gray-300">BMI</span>
                    <span>{r.bmi}</span>
                    <span className="font-medium text-gray-700 dark:text-gray-300">Activity</span>
                    <span className="capitalize">{r.activity_level}</span>
                  </div>
                  {r.health_risks && (
                    <p className="text-sm text-gray-600 dark:text-gray-400 mt-2 border-t border-gray-200 dark:border-gray-700 pt-2">
                      {r.health_risks}
                    </p>
                  )}
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
