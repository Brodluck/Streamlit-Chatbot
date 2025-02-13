# Chatbot Application

This repository contains two Streamlit-based chatbot applications:

1. **Normal Chatbot** (`normal_chatbot.py`): A simple text-based chatbot interface.  
2. **Chatbot with Images** (`chatbot_with_images.py`): A chatbot interface that can also handle image uploads when the vision-enabled model is selected.

Both apps use the [Groq](https://groq.com/) Python client to connect to various large language models.

---

## What Do These Apps Do?

### Normal Chatbot

- Allows you to select a model (e.g., `deepseek-r1-distill-llama-70b` or `qwen-2.5-32b`).  
- Prompts you for text input through a simple conversation interface.  
- Streams back a response from the selected model in real time.

### Chatbot with Images

- Similar to the Normal Chatbot, but also allows the user to upload an image **if** the selected model supports vision (`llama-3.2-90b-vision-preview`).  
- The uploaded image is converted to base64 and sent to the model, which can then analyze or comment on the image, depending on the model’s capabilities.  
- Streams back a response in real time.

Both chatbots store conversation history in a Streamlit session state, so the conversation persists as long as the session is active.

---

## Installation

1. **Clone or download** the repository to your local machine.

2. **Create and activate a virtual environment** (recommended). For example:
   ```python3 -m venv venv```
   ```source venv/bin/activate```

On Windows:
python -m venv venv
.\venv\Scripts\activate

3. **Install dependencies:**
pip install -r requirements.txt

Note: Make sure you have Python 3.7+ installed.

---

## Configuration
Before running either chatbot, make sure to set your GROQ_API_KEY environment variable so the application can authenticate with Groq. You can get your Groq API key from Groq.com.
For example:
- On macOS/Linux:
```export GROQ_API_KEY="your_api_key_here"```

- On Windows (Command Prompt):
```set GROQ_API_KEY="your_api_key_here"```

- On Windows (PowerShell):
```$env:GROQ_API_KEY="your_api_key_here"```

Alternatively, you can store this key in a file like .env (if you manage secrets that way) and load it in your environment. Or configure your .bashrc file
if you are working in linux or WSL.

---

## Usage

### Running the Normal Chatbot
1. **From the root directory of the project, run:**
```streamlit run normal_chatbot.py```
2. **A local URL (e.g., http://localhost:8501) will appear in the console. Open it in your browser.**
3. **Select the model you want to use from the dropdown.**
4. **Start using the chat!**

### Running the Chatbot with Images

1. **From the root directory of the project, run:**
```streamlit run chatbot_with_images.py```
2. **A local URL (e.g., http://localhost:8501) will appear in the console. Open it in your browser.**
3. **Select the model you want to use from the dropdown.**
    - If you pick llama-3.2-90b-vision-preview, you will see an option to upload an image.
4. **Type your message into the chat input box.**
5. **If you are using the vision model, optionally upload an image (PNG/JPG/JPEG) before sending your message.**