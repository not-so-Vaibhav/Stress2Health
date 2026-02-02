-- ============================================================
-- Stress2Health - Supabase Schema & Row Level Security (RLS)
-- Run this in Supabase SQL Editor: Dashboard → SQL Editor → New Query
-- ============================================================

-- 1. Create user_health_data table
-- Stores AI-predicted health results per user (one row per assessment)
-- ============================================================
CREATE TABLE IF NOT EXISTS public.user_health_data (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    stress_level TEXT NOT NULL,
    sleep_hours INTEGER NOT NULL,
    bmi NUMERIC(4,2) NOT NULL,
    activity_level TEXT NOT NULL,
    health_risks TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Index for fast lookups by user (for "view my history")
CREATE INDEX IF NOT EXISTS idx_user_health_data_user_id 
ON public.user_health_data(user_id);

-- Index for sorting by date
CREATE INDEX IF NOT EXISTS idx_user_health_data_created_at 
ON public.user_health_data(created_at DESC);

-- ============================================================
-- 2. Enable Row Level Security (RLS)
-- Users can ONLY access their own rows
-- ============================================================
ALTER TABLE public.user_health_data ENABLE ROW LEVEL SECURITY;

-- Policy: Users can INSERT only their own data (user_id must match logged-in user)
CREATE POLICY "Users can insert own health data"
ON public.user_health_data
FOR INSERT
TO authenticated
WITH CHECK (auth.uid() = user_id);

-- Policy: Users can SELECT only their own data
CREATE POLICY "Users can view own health data"
ON public.user_health_data
FOR SELECT
TO authenticated
USING (auth.uid() = user_id);

-- Policy: Users can UPDATE only their own data (optional, for future edits)
CREATE POLICY "Users can update own health data"
ON public.user_health_data
FOR UPDATE
TO authenticated
USING (auth.uid() = user_id)
WITH CHECK (auth.uid() = user_id);

-- Policy: Users can DELETE only their own data (optional)
CREATE POLICY "Users can delete own health data"
ON public.user_health_data
FOR DELETE
TO authenticated
USING (auth.uid() = user_id);

-- ============================================================
-- 3. Grant usage to authenticated users
-- ============================================================
GRANT ALL ON public.user_health_data TO authenticated;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO authenticated;
