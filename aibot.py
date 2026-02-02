import streamlit as st
from google import genai
from google.genai import types
import os #reading environment variables
from dotenv import load_dotenv #environment variables

load_dotenv() #loads the environment variables

api_key = os.getenv("GOOGLE_API_KEY")

st.title("AI Document Assistant")

if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=api_key)   #st.session_state.client is a variable saved in session

with st.sidebar:
    st.header("Setup")
    uploaded_file_ui = st.file_uploader("Upload your document", type=["pdf", 'txt'])

    if uploaded_file_ui and "doc_ref" not in st.session_state:
        with st.spinner("Uploading document..."):
        #we need to check the file type
            mime_type = uploaded_file_ui.type

        #writing the bytes to a temporary file
        with open("temp_doc", "wb") as f: #created a temp_doc file with writing capabilities
            f.write(uploaded_file_ui.getbuffer())

        doc_ref = st.session_state.client.files.upload(
            file="temp_doc",
            config={"mime_type": mime_type}
        )
        st.session_state.doc_ref = doc_ref

        st.session_state.chat =st.session_state.client.chats.create(
            model="gemini-3-flash-preview",
            config= types.GenerateContentConfig(
                system_instruction="You are a document expert assistant."
                                    "Answer questions ONLY using the uploaded file."
                                    "If the answer isn't there, say you don't know."
            )
        )
    st.success("Document uploaded succesfully!")
if "messages" not in st.session_state:
    st.session_state.messages = [] #creating a list of dictionaries where each dictionary is a message contatining a role and content

for msg in st.session_state.messages:    #iterate through the list of dictionaries
    with st.chat_message(msg["role"]): #create a div block for each role
        st.markdown(msg["Content"])    #print the content so youre able to see the entire history of the coversation

prompt = st.chat_input("Ask a question about the uploaded document:")
if prompt:
    if "chat" not in st.session_state:
        st.error("Please upload a document first!")
    else:
        st.session_state.messages.append({"role":"user",
                                    "content":prompt})
    with st.chat_message("user",avatar="👨‍💻"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(
            message=[st.session_state.doc_ref, prompt]
        )
    st.markdown(response.text)
    st.session_state.messages.append({"role":"assistant",
                                      "content":response.text})


