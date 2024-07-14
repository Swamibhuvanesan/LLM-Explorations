# Voice Assistant with Streamlit

This project is a voice assistant web application built using Streamlit, Google Generative AI, SpeechRecognition, and pyttsx3. It listens to your voice, processes the input, and provides a spoken response. Additionally, it offers an option to pause the narration.

## Features

- **Voice Input**: Listen to user queries via microphone.
- **Generative AI Response**: Uses Google's Generative AI to process and respond to queries.
- **Text-to-Speech**: Provides spoken responses using pyttsx3.
- **Pause Narration**: Option to pause the narration of responses.
- **Conversation Management**: Ability to exit the conversation and start a new one.

## Requirements

- Python 3.7 or higher
- Streamlit
- SpeechRecognition
- pyttsx3
- google-generativeai
- PortAudio (for SpeechRecognition)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Swamibhuvanesan/LLM-Explorations.git
    cd LLM-Explorations
    ```

2. **Install the required packages:**
    ```bash
    pip install -m requirements.txt
    ```


3. **Set up Google Generative AI API:**
    - Sign up for the API and get your API key from [Google Cloud Console](https://console.cloud.google.com/apis/credentials).

4. **Add your API key:**
    Replace `API_KEY` in the code with your actual API key.

## Usage

1. **Run the Streamlit app:**
    ```bash
    streamlit run bot.py
    ```

2. **Interact with the app:**
    - Click on **Listen** to start recording your voice.
    - The app will display your input and the bot's response in text areas.
    - Check the **Pause Narration** checkbox if you want to pause the spoken responses.
    - Click on **Exit Conversation** to end the current conversation and start a new one.

## Project Structure

```plaintext
.
├── bot.py          # Main script for the Streamlit app
├── requirements.txt # List of required Python packages
└── README.md       # This readme file

## Screenshot
