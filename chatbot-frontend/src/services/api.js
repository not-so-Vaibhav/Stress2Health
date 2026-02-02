const CHAT_STORAGE_KEY = "stress2health_chat";

export function getStoredChat() {
  try {
    const raw = localStorage.getItem(CHAT_STORAGE_KEY);
    if (!raw) return null;
    const data = JSON.parse(raw);
    if (data?.messages?.length) return data;
    return null;
  } catch {
    return null;
  }
}

export function saveChat(messages, sessionId) {
  try {
    localStorage.setItem(
      CHAT_STORAGE_KEY,
      JSON.stringify({ messages, sessionId, savedAt: Date.now() })
    );
  } catch {}
}

export function clearStoredChat() {
  try {
    localStorage.removeItem(CHAT_STORAGE_KEY);
  } catch {}
}

export async function sendMessage(message, sessionId = null) {
  try {
    const response = await fetch("http://localhost:5001/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message, session_id: sessionId }),
    });

    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      throw new Error(errorData.error || "Unable to connect to AI service");
    }

    const data = await response.json();
    if (data.error) throw new Error(data.error);

    return {
      reply: data.reply || "I'm here to help! Could you tell me more?",
      sessionId: data.session_id ?? null,
      healthData: data.health_data ?? null, // Present when assessment completes (for Supabase save)
    };
  } catch (error) {
    if (error instanceof TypeError && error.message.includes("fetch")) {
      throw new Error(
        "Unable to connect to backend. Make sure it's running on port 5001."
      );
    }
    throw error;
  }
}
