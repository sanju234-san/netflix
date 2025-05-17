import streamlit as st
from ibm_watson import AssistantV2, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import base64

# Watson Assistant setup
assistant_auth = IAMAuthenticator(st.secrets["ibm"]["apikey"])
assistant = AssistantV2(version="2021-06-14", authenticator=assistant_auth)
assistant.set_service_url(st.secrets["ibm"]["url"])
assistant_id = st.secrets["ibm"]["assistant_id"]

# Watson TTS setup
tts_auth = IAMAuthenticator(st.secrets["ibm_tts"]["apikey"])
tts = TextToSpeechV1(authenticator=tts_auth)
tts.set_service_url(st.secrets["ibm_tts"]["url"])

# Streamlit page config
st.set_page_config(page_title="IBM AI Chatbot with Voice")
st.title("🗣️ IBM Watson AI Chatbot with Multilingual Voice")

# Language/voice selector
lang_voice_map = {
    "English": "en-US_MichaelV3Voice",
    "Hindi": "hi-IN_MadhurV3Voice",
    "Spanish": "es-ES_EnriqueV3Voice",
    "French": "fr-FR_ReneeV3Voice",
    "German": "de-DE_DieterV3Voice"
}
language = st.selectbox("Choose response language", list(lang_voice_map.keys()))
voice = lang_voice_map[language]

# Session & chat history
if "session_id" not in st.session_state:
    session = assistant.create_session(assistant_id=assistant_id).get_result()
    st.session_state.session_id = session["session_id"]
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    role = "🧑 You" if msg["role"] == "user" else "🤖 Bot"
    st.markdown(f"**{role}:** {msg['content']}")

# Input field
user_input = st.text_input("You:", key="user_input")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get chatbot response
    response = assistant.message(
        assistant_id=assistant_id,
        session_id=st.session_state.session_id,
        input={"message_type": "text", "text": user_input}
    ).get_result()

    if response["output"]["generic"]:
        bot_reply = response["output"]["generic"][0]["text"]
    else:
        bot_reply = "I'm not sure how to respond."

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.markdown(f"**🤖 Bot:** {bot_reply}")

    # Convert text to speech
    audio = tts.synthesize(
        bot_reply,
        voice=voice,
        accept='audio/mp3'
    ).get_result().content

    # Encode and play audio
    b64_audio = base64.b64encode(audio).decode()
    st.audio(f"data:audio/mp3;base64,{b64_audio}", format="audio/mp3")
