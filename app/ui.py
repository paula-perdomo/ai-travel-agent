import streamlit as st
import requests

# --- CONFIGURATION ---
BASE_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Travel Agent", page_icon="✈️")

# --- SESSION STATE INITIALIZATION ---
if "page" not in st.session_state:
    st.session_state.page = "landing"

if "messages" not in st.session_state:
    st.session_state.messages = []

# --- PAGE 1: LANDING PAGE ---
if st.session_state.page == "landing":
    st.title("AI Travel Agent 🌍")
    st.write("Ready to plan your next adventure?")
    
    if st.button("Start"):
        with st.spinner("Connecting to Agent..."):
            try:
                # 1. Call your GET endpoint to get the intro
                response = requests.get(f"{BASE_URL}/get_agent_intro")
                
                if response.status_code == 200:
                    intro_text = response.json().get("response")
                    
                    # Save the intro to chat history
                    st.session_state.messages.append({"role": "model", "content": intro_text})
                    
                    # Switch to chat page
                    st.session_state.page = "chat"
                    st.rerun()
                else:
                    st.error(f"Error getting intro: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("Could not connect to backend. Is it running?")

# --- PAGE 2: CHAT INTERFACE ---
elif st.session_state.page == "chat":
    st.header("Chat with Atlas ✈️")

    # A. Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # B. Input Box
    user_input = st.chat_input("Type your message here...")

    # C. Handle User Input
    if user_input:
        # 1. Display User Message Immediately
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 2. Call your POST endpoint
        with st.spinner("Thinking..."):
            try:
                # NOTE: In FastAPI, 'def send_message(message:str)' expects a query param.
                # We use 'params=' instead of 'json='
                response = requests.post(
                    f"{BASE_URL}/send_message", 
                    json={"message": user_input} 
                )
                
                if response.status_code == 200:
                    agent_response = response.json().get("response")
                    
                    # 3. Display Agent Response
                    with st.chat_message("model"):
                        st.markdown(agent_response)
                    st.session_state.messages.append({"role": "model", "content": agent_response})
                else:
                    st.error(f"Server Error: {response.text}")

            except requests.exceptions.ConnectionError:
                st.error("Lost connection to the backend.")