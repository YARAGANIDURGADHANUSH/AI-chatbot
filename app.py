import streamlit as st
from groq import Groq

# Set your API key
client = Groq(api_key="YOUR_API_KEY")

st.title("Mini AI Chatbot 🤖")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": reply})

# Display chat
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write("🧑 You:", msg["content"])
    else:
        st.write("🤖 Bot:", msg["content"])
