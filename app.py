from email.mime import audio
import os
import streamlit as st
import google.generativeai as genai
# from google.cloud import texttospeech

os.environ["GOOGLE_API_KEY"] = "AIzaSyCtF9ZrpFty_2LnjknOnaxA9GJ1L4XhiA8"

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# tts_client = texttospeech.TextToSpeechClient()

# def text_to_speech(text):
#     synthesis_input = texttospeech.SynthesisInput(text=text)
#     voice = texttospeech.VoiceSelectionParams(
#         language_code="en-US", 
#         ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
#     )
#     audio_config = texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3
#     )

#     response = tts_client.synthesize_speech(
#         input=synthesis_input, 
#         voice=voice, 
#         audio_config=audio_config
#     )

    # with open("output.mp3", "wb") as out:
    #     out.write(response.audio_content)
    # os.system("mpg321 output.mp3")  

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

st.title("Chat with Google Gemini-Pro!")

def role_to_streamlit(role):
    if role == "model":
        return "assistant"
    else:
        return role

for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("How may I assist you today? "):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    # text_to_speech(response.text)  