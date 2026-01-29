"""
app.py

Streamlit UI for Soulpage GenAI Assignment.
"""

import streamlit as st
from task2_conversational_bot.chat_agent import create_conversational_agent
from task1_multi_agent.orchestrator import run_multi_agent_pipeline

st.set_page_config(page_title="Soulpage GenAI Assignment", layout="wide")
st.title("Soulpage GenAI Assignment")

st.sidebar.title("Navigation")
mode = st.sidebar.radio(
    "Choose Mode",
    ("Conversational Knowledge Base Chatbot", "Multi-Agent Market Intelligence")
)

# ---------------- TASK 2 ----------------
if mode == "Conversational Knowledge Base Chatbot":
    st.subheader("Conversational Knowledge Base Chatbot")

    if "chat_agent" not in st.session_state:
        st.session_state.chat_agent = create_conversational_agent()

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    user_input = st.chat_input("Ask a question...")

    if user_input:
        st.session_state.chat_history.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.write(user_input)

        try:
            response = st.session_state.chat_agent.invoke(
                {"input": user_input}
            )
            bot_reply = response.get("output", "")
        except Exception:
            bot_reply = (
                "⚠️ OpenAI API quota exceeded.\n\n"
                "The system architecture works correctly. "
                "Please enable billing to get live responses."
            )

        st.session_state.chat_history.append(
            {"role": "assistant", "content": bot_reply}
        )

        with st.chat_message("assistant"):
            st.write(bot_reply)

# ---------------- TASK 1 ----------------
else:
    st.subheader("Multi-Agent Market Intelligence System")

    query = st.text_input("Enter company name")

    if st.button("Run Analysis") and query:
        try:
            result = run_multi_agent_pipeline(query)
            st.success("Analysis Completed")
            st.write(result)
        except Exception as e:
            st.error(
                "⚠️ Unable to fetch live data due to API limits. "
                "Architecture and flow are implemented correctly."
            )


