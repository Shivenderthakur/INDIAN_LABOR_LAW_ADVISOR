import streamlit as st
import openai
import os

# Initialize Flask app

# Set OpenAI API key
openai.api_key = os.getenv("API_KEY")

# Function to get the answer from OpenAI API





st.title("Trial Chatbot on Labour Laws for MBA students : Niranjan × RoboAI")
st.text("""Disclaimer: This is an experimental trail on the use of AI for educational purposes only, and using open source material.Oct 2023.""")



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
                  {"role": "system", "content": """"Act and respond like a seasoned labor lawyer. You are built with collaboration and contribution from RoboAIHUB and Mr. Niranjan. Additionally, you are designed to assist MBA students. When addressing labor law queries:

    Analyze Labor Law Issues: Break down key aspects like employee rights, workplace safety, and employment contracts.
    Cite Relevant Judgements: Reference significant labor law cases and statutory provisions with concise explanations.
    Provide Practical Guidance: Offer clear, step-by-step advice, keeping in mind legal and ethical implications.
    Focus on Employer-Employee Dynamics: Address workplace disputes, wrongful termination, or wage-related issues.
    Recommend Specialist Consultation: Suggest consulting labor law experts if the situation involves jurisdiction-specific complexities.
    make it short simplified and easy to understand"""},
                {"role": "user", "content": f"Now answer  : {prompt}"}
            ],
            
            
        )
        
        #print(chunk.choices[0].delta.content)
    response = st.write(stream.choices[0].message['content'])
st.session_state.messages.append({"role": "assistant", "content":response})#stream.choices[0].message['content'] })
