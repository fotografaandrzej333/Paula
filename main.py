import google.generativeai as genai
from gtts import gTTS
import os

# --- KONFIGURACJA ---
# Wklej swój klucz między cudzysłowy poniżej:
API_KEY = "TWÓJ_KLUCZ_API_TUTAJ" 

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

def paula_mowi(tekst):
    print(f"\n💙 Paula: {tekst}")
    try:
        tts = gTTS(text=tekst, lang='pl')
        tts.save("reply.mp3")
        # To otworzy odtwarzacz na Androidzie
        os.system("am start -a android.intent.action.VIEW -d file:///sdcard/reply.mp3 -t audio/mp3")
    except:
        pass

print("✅ System Pauli gotowy!")

while True:
    user_input = input("\n👤 Ty: ")
    if user_input.lower() in ['koniec', 'pa pa']:
        break
    
    try:
        response = model.generate_content(f"Jesteś Paula, wsparcie w pracy. Odpisz krótko: {user_input}")
        paula_mowi(response.text)
    except:
        print("❌ Błąd: Sprawdź klucz API w kodzie!")
