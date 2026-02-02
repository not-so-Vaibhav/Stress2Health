/**
 * Supabase health data service
 * Insert and fetch user_health_data (RLS ensures users only see their own rows)
 */
import { supabase } from '../lib/supabase';

/**
 * Save health assessment result to Supabase
 * @param {Object} healthData - { stress_level, sleep_hours, bmi, activity_level, health_risks }
 * @param {string} userId - auth.users.id (from session.user.id)
 * @returns {Object} { data, error }
 */
export async function saveHealthData(healthData, userId) {
  if (!supabase || !userId) {
    return { data: null, error: new Error('Supabase or user not available') };
  }

  const { data, error } = await supabase
    .from('user_health_data')
    .insert({
      user_id: userId,
      stress_level: healthData.stress_level,
      sleep_hours: healthData.sleep_hours,
      bmi: healthData.bmi,
      activity_level: healthData.activity_level,
      health_risks: healthData.health_risks,
    })
    .select('id, created_at')
    .single();

  return { data, error };
}

/**
 * Fetch all health records for the logged-in user (RLS filters by user_id)
 * @returns {Object} { data: [...], error }
 */
export async function fetchHealthHistory() {
  if (!supabase) {
    return { data: [], error: new Error('Supabase not configured') };
  }

  const { data, error } = await supabase
    .from('user_health_data')
    .select('id, stress_level, sleep_hours, bmi, activity_level, health_risks, created_at')
    .order('created_at', { ascending: false });

  return { data: data ?? [], error };
}
