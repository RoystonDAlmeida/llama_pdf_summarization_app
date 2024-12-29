import PyPDF2
import streamlit as st
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Set up your ChatGroq model configuration
llm = ChatGroq(model_name="llama-3.1-70b-versatile", temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"))

# Define the Streamlit app layout
st.title("Custom Summarization App with ChatGroq's LLaMA")

custom_prompt = st.text_area("Enter your custom summary prompt",
                              "Summarize the following text:")
uploaded_file = st.file_uploader("Upload a PDF document", type="pdf")

# Function to read PDF and extract text
def read_pdf(file):
    """
    @Args:- file:- file object corresponding to a PDF
    @Description:-
                This method extracts all the text from a PDF document
    @Returns:- text:- str object containing text of the PDF document
    """

    pdf_reader = PyPDF2.PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text() + "\n"
    return text

# Function to summarize the document
def summarize_document(text, custom_prompt):
    """
    @Args:- text:- str object containing PDF text,
            custom_prompt:- str object containing the prompt
    @Description:-
                This method splits the PDF into text and summarizes
                chunks of text
    @Returns:- summaries:- list object containing summaries of chunks of text
    """

    # Split the text into manageable chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = text_splitter.split_text(text)

    # Create a prompt template for summarization
    prompt_template = PromptTemplate(template = custom_prompt+"\n\n{chunk}", input_variables=["chunk"])

    # Create a list to hold summaries
    summaries = []

    # Summarize each chunk of text using the LLaMA model
    for chunk in chunks:
        chain = LLMChain(llm=llm, prompt = prompt_template)
        summary = chain.run({"chunk": chunk})
        summaries.append(summary)

    return summaries

# Handle file upload and summarization
if st.button("Summarize"):
    if uploaded_file is not None:
        # Read and extract text from the uploaded PDF file
        pdf_text = read_pdf(uploaded_file)

        if pdf_text.strip(): # Check if there is any extracted text
            summaries = summarize_document(pdf_text, custom_prompt)

            for idx, summary in enumerate(summaries):
                st.subheader(f"Summary {idx + 1}")
                st.write(summary)

        else:
            st.error("No text found in the PDF file")

    else:
        st.error("Please upload a PDF document")