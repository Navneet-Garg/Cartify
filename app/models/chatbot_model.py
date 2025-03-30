import google.generativeai as genai
from app.config.settings import GOOGLE_API_KEY

# Configure the Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")
chat = model.start_chat(history=[])

def get_gemini_response(message):
    response = chat.send_message(message, stream=True)
    formatted_response = "\n".join([chunk.text for chunk in response])  # Preserve newlines
    return formatted_response