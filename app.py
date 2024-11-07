import streamlit as st
import openai
import os

# Initialize Flask app

# Set OpenAI API key
openai.api_key = "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"#os.getenv("API_KEY")

# Function to get the answer from OpenAI API
def get_labour_law_answer(question):
    prompt = f"Based on Indian labor law, answer the following question in a clear and concise manner and structured output : {question}"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",  # Or whichever model you're using
            messages=[
                {"role": "system", "content": "You are a legal labor law advisor specialized in Indian labor law.Never go out of the scope.act and respond like a professional indian lawyer in labor laws, Keep the details list provide most important information first.you are build for NLU Jodhpur"},
                {"role": "user", "content": prompt}
            ]
            
        )

        # Extract the response text
        answer = response.choices[0].message['content']
        
         # Format the answer into structured components
        return answer


    except Exception as e:
        return str(e)

# Route for handling chatbot requests


import streamlit as st

st.title("Labor Law Advisor : NLU Jdh  ")



if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask things realted to the Labor law"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("Legal Advisor"):
        stream = openai.ChatCompletion.create(
            model="gpt-4-0125-preview",  # Or whichever model you're using
            messages=[
                  {"role": "system", "content": "You are a legal labor law advisor specialized in Indian labor law.Never go out of the scope.act and respond like a professional indian lawyer in labor laws, Keep the explaination short in points with heading and total world limit upto 100 words list provide most important information first.you are build for NLU Jodhpur"},
                {"role": "user", "content": f"Based on Indian labor law, answer the following question in a clear and concise manner and structured output : {prompt}"}
            ],
            
            
        )
        #print(chunk.choices[0].delta.content)
        response = st.write(stream.choices[0].message['content'])
    st.session_state.messages.append({"role": "assistant", "content":stream.choices[0].message['content'] })
