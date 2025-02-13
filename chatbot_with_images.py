import streamlit as st
from groq import Groq
import base64

def generate_response(messages, model):
    client = Groq()
    completion = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.6,
        top_p=0.95,
        stream=True,
        stop=None,
    )

    full_response = ""
    placeholder = st.empty()
    for chunk in completion:
        delta = chunk.choices[0].delta.content or ""
        full_response += delta
        placeholder.markdown(full_response)
    placeholder.empty()
    return full_response

def main():
    st.title("Chatbot")

    selected_model = st.selectbox(
        "Select the model to use:",
        options=[
            "deepseek-r1-distill-llama-70b",
            "llama-3.2-90b-vision-preview",
            "qwen-2.5-32b"
        ]
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        role = message["role"]
        content = message["content"]
        
        with st.chat_message(role):
            if isinstance(content, list):
                for part in content:
                    if part["type"] == "text":
                        st.write(part["text"])
                    elif part["type"] == "image_url":
                        st.image(part["image_url"]["url"])
            else:
                st.write(content)

    uploaded_image = None
    if selected_model == "llama-3.2-90b-vision-preview":
        uploaded_image = st.file_uploader("Sube una imagen (solo para el modelo de visión)", 
                                          type=['png', 'jpg', 'jpeg'])

    user_input = st.chat_input("Escribe tu mensaje:")
    if user_input:
        user_content = []
        user_content.append({"type": "text", "text": user_input})

        if uploaded_image:
            image_bytes = uploaded_image.read()
            base64_image = base64.b64encode(image_bytes).decode('utf-8')
            mime_type = uploaded_image.type
            user_content.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:{mime_type};base64,{base64_image}"
                }
            })

        st.session_state.messages.append({
            "role": "user",
            "content": user_content
        })

        with st.chat_message("user"):
            for part in user_content:
                if part["type"] == "text":
                    st.write(part["text"])
                elif part["type"] == "image_url":
                    st.image(part["image_url"]["url"])

        with st.spinner("Generando respuesta..."):
            response = generate_response(st.session_state.messages, selected_model)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
        st.chat_message("assistant").write(response)

if __name__ == "__main__":
    main()
