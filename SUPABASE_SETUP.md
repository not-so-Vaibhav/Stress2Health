# Supabase Setup Guide - Stress2Health

## 1. Create Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign in
2. Click **New Project**
3. Name it (e.g. `stress2health`), set password, choose region
4. Wait for project to be created

## 2. Run the SQL Schema

1. In Supabase Dashboard, go to **SQL Editor** → **New Query**
2. Copy the contents of `supabase/schema.sql`
3. Paste and click **Run**
4. You should see "Success" - this creates `user_health_data` table and RLS policies

## 3. Enable Email Auth

1. Go to **Authentication** → **Providers**
2. **Email** is enabled by default
3. (Optional) Disable "Confirm email" in **Authentication** → **Settings** if you want instant signup without email verification for testing

## 4. Get API Keys

1. Go to **Project Settings** (gear icon) → **API**
2. Copy:
   - **Project URL** → `VITE_SUPABASE_URL`
   - **anon public** key → `VITE_SUPABASE_ANON_KEY`

## 5. Configure Frontend

1. In `chatbot-frontend/`, copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and paste your URL and anon key:
   ```
   VITE_SUPABASE_URL=https://xxxxx.supabase.co
   VITE_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
   ```

## 6. Install & Run

```bash
cd chatbot-frontend
npm install
npm run dev
```

## Flow Summary

1. **Without .env**: App runs in guest mode (no auth, no Supabase save)
2. **With .env**: Login/Signup required → Chat → Assessment completes → Data saved to Supabase → View History

## RLS (Row Level Security)

- Users can **INSERT** only their own `user_id`
- Users can **SELECT** only their own rows
- Users can **UPDATE/DELETE** only their own rows
- Enforced by Supabase at the database level
