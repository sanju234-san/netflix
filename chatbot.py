import streamlit as st
from ibm_watson import AssistantV1, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import tempfile
import os
import pygame

# IBM Watson Assistant Credentials (V1 - Dialog)
assistant_api_key = '6cmuCiCMWg6oZgSDMb7edxZ_HIS8aOKlpLjDGVIaLYez'
assistant_url = 'https://api.us-south.assistant.watson.cloud.ibm.com'
workspace_id = '16021a45-9cda-40d8-9761-28c9ad153b85'  # Dialog skill (not action skill)

# IBM Watson Text-to-Speech Credentials
tts_api_key = 'L4HZiCdP0js74Zh257CksORqJ8VF_QPQsk-Y38yWBTtX'
tts_url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/fe0d7bfd-be8c-4605-9cca-89ecac74502a'

# Setup Assistant
assistant_auth = IAMAuthenticator(assistant_api_key)
assistant = AssistantV1(
    version='2021-06-14',
    authenticator=assistant_auth
)
assistant.set_service_url(assistant_url)

# Setup Text to Speech
tts_auth = IAMAuthenticator(tts_api_key)
text_to_speech = TextToSpeechV1(authenticator=tts_auth)
text_to_speech.set_service_url(tts_url)

# Play audio using pygame
def speak_text(text):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as audio_file:
        audio_content = text_to_speech.synthesize(
            text,
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'
        ).get_result().content
        audio_file.write(audio_content)
        audio_path = audio_file.name

    # Play using pygame
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    except Exception as e:
        st.error(f"Audio playback error: {e}")

# Streamlit App
st.title("🤖 IBM Watson Chatbot with Voice")

user_input = st.text_input("You:", "")

if user_input:
    response = assistant.message(
        workspace_id=workspace_id,
        input={'text': user_input}
    ).get_result()

    try:
        bot_reply = response['output']['text'][0]
    except (KeyError, IndexError):
        bot_reply = "I didn't understand that. Try again."

    st.text_area("Watson:", bot_reply, height=100)
    
    if st.button("🔊 Speak Reply"):
        speak_text(bot_reply)
