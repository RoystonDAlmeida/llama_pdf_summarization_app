# Custom Summarization App with ChatGroq's LLaMA

## Overview

This is a custom summarization application built with Streamlit and LangChain. It uses ChatGroq's LLaMA model to generate summaries from PDF documents uploaded by users.

## Features

- Upload PDF documents for summarization.
- Enter custom prompts to guide the summarization process.
- User-friendly interface powered by Streamlit.

## Requirements

- Python 3.9 or higher
- ChatGroq API key
- Required Python packages:
  - `streamlit`
  - `langchain`
  - `langchain-groq`
  - `PyPDF2`

## Installation

1. **Clone the Repository**

    ```bash
    git clone git@github.com:RoystonDAlmeida/llama_pdf_summarization_app.git
    cd llama_pdf_summarization_app/
   ```

2. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
   ```

3. **Set Up Your API Key**

Set your ChatGroq API key in your environment:

```
GROQ_API_KEY = 
```

## Usage

1. **Run the Application**

    ```bash
    streamlit run pdf_summarization.py
    ```

2. **Open the App**

Go to `http://localhost:8501` in your web browser.

3. **Upload a PDF Document**

4. **Enter a Custom Summary Prompt**

5. **Click "Summarize"** to generate summaries.