import streamlit as st
import speech_recognition as sr
import pyttsx3
import google.generativeai as genai

# Directly assign the API key
API_KEY = "AIzaSyBVN4FiHyg_6T1bFoZfV8nte1LmyDxBrGo"

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = "In this chat, respond professionally and in more detail."

def send_message(question):
    """Send a question to the AI model and return the response."""
    if question.strip() == '':
        return "Please ask something."
    response = chat.send_message(instruction + question)
    return response.text

def exit_conversation():
    """End the current conversation and reset the chat history."""
    chat.history = []
    st.session_state['conversation_ended'] = True

def listen():
    """Listen for a voice input, process it, and get a response from the AI model."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.session_state['status'] = "Listening..."
        audio = recognizer.listen(source)

    try:
        question = recognizer.recognize_google(audio)
        st.session_state['user_input'] = question
        if question.lower() == "exit":
            exit_conversation()
            st.write("Conversation terminated. Say 'Listen' to start again.")
            st.session_state['status'] = "Conversation terminated"
            return
        st.session_state['status'] = "Processing..."
        response = send_message(instruction + question)
        st.session_state['bot_response'] = response
        
        if not st.session_state.get('pause_narration', False):
            # Initialize the TTS engine and say the response
            engine = pyttsx3.init()
            engine.say(response)
            engine.runAndWait()
        
        st.session_state['status'] = "Ready"
    except sr.UnknownValueError:
        st.error("Could not understand the audio")
        st.session_state['status'] = "Error: Could not understand audio"
    except sr.RequestError as e:
        st.error(f"Could not request results: {e}")
        st.session_state['status'] = f"Error: Could not request results"

def main():
    """Main function to run the Streamlit app."""
    st.set_page_config(page_title="Voice Assistant", page_icon=":robot_face:")
    st.markdown(
        """
        <style>
        .main {
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
        }
        .title {
            font-size: 32px;
            color: #4CAF50;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .status {
            font-size: 18px;
            color: #FF5733;
            margin-bottom: 10px;
        }
        textarea {
            width: 100% !important;
            max-width: 100% !important;
        }
        </style>
        """, unsafe_allow_html=True
    )

    st.markdown("<div class='title'>Voice Assistant</div>", unsafe_allow_html=True)

    if 'conversation_ended' not in st.session_state:
        st.session_state['conversation_ended'] = False

    if 'status' not in st.session_state:
        st.session_state['status'] = "Ready"

    if 'pause_narration' not in st.session_state:
        st.session_state['pause_narration'] = False

    st.markdown(f"<div class='status'>{st.session_state['status']}</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Listen"):
            listen()
    with col2:
        if st.button("Exit Conversation"):
            exit_conversation()
            st.write("Conversation terminated. Say 'Listen' to start again.")
    
    st.checkbox("Pause Narration", key='pause_narration')

    st.text_area("You:", value=st.session_state.get("user_input", ""), height=200, placeholder="Your voice input will appear here...", help="This is what you said.")
    st.text_area("Bot:", value=st.session_state.get("bot_response", ""), height=200, placeholder="The bot's response will appear here...", help="This is the bot's response.")

if __name__ == "__main__":
    main()
