import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
gemini_key = os.getenv("GEMINI_API_KEY")

print("Supabase URL loaded:", bool(supabase_url))
print("Supabase key loaded:", bool(supabase_key))
print("Gemini key loaded:", bool(gemini_key))