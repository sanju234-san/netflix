import streamlit as st
from ibm_watson import AssistantV2, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# 🔐 Hardcoded IBM Watson credentials (ONLY for testing)
IBM_API_KEY = "6cmuCiCMWg6oZgSDMb7edxZ_HIS8aOKlpLjDGVIaLYez"
IBM_ASSISTANT_URL = "https://api.us-south.assistant.watson.cloud.ibm.com/instances/8763f5c8-7b72-453e-bb7c-44bd7e75ed80"
IBM_ASSISTANT_ID = "4416391a-7896-4764-b0fb-e0b6dcd68214"

# Authenticator
assistant_auth = IAMAuthenticator(IBM_API_KEY)

# Assistant Service
assistant = AssistantV2(
    version='2021-06-14',
    authenticator=assistant_auth
)
assistant.set_service_url(IBM_ASSISTANT_URL)

# Create session
session_id = assistant.create_session(assistant_id=IBM_ASSISTANT_ID).get_result()["session_id"]

# Streamlit UI
st.title("IBM Watson Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Say something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Watson Response
    response = assistant.message(
        assistant_id=IBM_ASSISTANT_ID,
        session_id=session_id,
        input={"message_type": "text", "text": prompt}
    ).get_result()

    reply = response["output"]["generic"][0]["text"]
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
