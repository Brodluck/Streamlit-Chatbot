import streamlit as st
from groq import Groq

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
            "qwen-2.5-32b"
        ]
    )

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])

    user_input = st.chat_input("Type your message:")
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.chat_message("user").write(user_input)

        with st.spinner("Generating response..."):
            response = generate_response(st.session_state.messages, selected_model)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

if __name__ == "__main__":
    main()
