import streamlit as st
import requests
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv(dotenv_path=Path(".") / ".env")

API_URL = "https://router.huggingface.co/v1/chat/completions"
HEADERS = {"Authorization": f"Bearer {os.getenv('HUGGINGFACEHUB_API_TOKEN')}"}

# --- Function to query Hugging Face Router ---
def query_hf(messages):
    payload = {
        "model": "meta-llama/Llama-3.2-1B-Instruct",
        "messages": messages,
        "max_tokens": 300,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code != 200:
        return f"[Erreur API {response.status_code}] {response.text}"

    data = response.json()
    return data["choices"][0]["message"]["content"]


# --- Streamlit UI ---
st.set_page_config(page_title="Chatbot HF", page_icon="🤖")

st.title("🤖 Chatbot Hugging Face — API Router")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Bonjour Leana, comment puis-je t’aider aujourd’hui ?"}
    ]

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "assistant":
        st.chat_message("assistant").write(msg["content"])
    else:
        st.chat_message("user").write(msg["content"])

# User input
user_input = st.chat_input("Écris ton message ici…")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    # Query HF
    assistant_reply = query_hf(st.session_state.messages)

    # Add assistant reply
    st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    st.chat_message("assistant").write(assistant_reply)
