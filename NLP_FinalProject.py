import streamlit as st


if 'clicked' not in st.session_state:
	st.session_state.clicked = False

def set_clicked():
	st.session_state.clicked = True

st.title("Resumen")

audios = {"MA1.m4a":st.write}

choice = st.sidebar.selectbox('Selecciona un audio: ',['MA1.m4a'])

st.sidebar.button('Audio',on_click=set_clicked)
if st.session_state.clicked:
	if choice != '_':
		result = audios[choice](f'You choose {choice}')


import ssl
import certifi

ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
import ssl
print(ssl.get_default_verify_paths())

import openai
import whisper

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
openai.api_key = "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"

def load_whisper_model():
    try:
        model = whisper.load_model("base")
        return model
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        return None

def transcribe_audio(model, file_path):
    try:
        transcript = model.transcribe(file_path)
        return transcript['text']
    except Exception as e:
        print(f"Error during transcription: {e}")
        return ""

def custom_chatgpt(user_input):
    messages = [{"role": "system", "content": "You are an office administrator, summarize the text in key points"}]
    messages.append({"role": "user", "content": user_input})
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        chatgpt_reply = response["choices"][0]["message"]["content"]
        return chatgpt_reply
    except Exception as e:
        print(f"Error in ChatGPT response: {e}")
        return ""

import time
#Main Execution
model = load_whisper_model()
if model:
    progress_bar = st.progress(0)

# Simulando un proceso
    for percent_complete in range(100):
        time.sleep(0.1)  # Simula una tarea que tarda un poco
        progress_bar.progress(percent_complete + 1)

    st.success('¡Tarea completada!')
    
    file_path = choice
    transcription = transcribe_audio(model, file_path)
    summary = custom_chatgpt(transcription)
    st.write(summary)


