import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

# Configuration for LangGraph – unique thread ID per session
CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# Initialize message history in session state
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

# Display previous messages in the chat UI
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])  # Using markdown for better formatting

# Chat input field for user
user_input = st.chat_input('Type here')

if user_input:
    # Save user message to session history
    st.session_state['message_history'].append({
        'role': 'user',
        'content': user_input
    })

    # Display user message immediately
    with st.chat_message('user'):
        st.markdown(user_input)

    # Start assistant response with streaming
    with st.chat_message('assistant'):
        # Create an empty placeholder to stream content into
        response_placeholder = st.empty()
        full_response = ""

        # Stream response from LangGraph LLM agent
        ai_stream = chatbot.stream(
            {
                'messages': [HumanMessage(content=user_input)]  # Must be a list of messages
            },
            config=CONFIG,
            stream_mode='messages'  # Always use 'messages'
        )

        # Collect tokens as they stream in
        for message_chunk, _ in ai_stream:
            if message_chunk.content:  # Only update if content exists
                full_response += message_chunk.content
                response_placeholder.markdown(full_response)  # Update UI progressively

    # Save assistant's full response to session history
    st.session_state['message_history'].append({
        'role': 'assistant',
        'content': full_response
    })
