# RAG Demo with Google Generative AI, LangChain, and Streamlit

This project demonstrates a Retrieval-Augmented Generation (RAG) system that uses Google's Generative AI models, LangChain for orchestration, and Streamlit for the user interface. It can answer questions based on the content of uploaded PDF documents.

## Features

- **PDF Document Processing**: Upload PDF files to be used as the knowledge base.
- **Text Chunking and Embedding**: Splits documents into manageable chunks and creates vector embeddings.
- **Vector Store**: Uses FAISS for efficient similarity searches.
- **Question Answering**: Ask questions and get answers generated from the document content.
- **Simple and Interactive UI**: Built with Streamlit for ease of use.

## Project Structure

```
.
├── .gitignore
├── my_env/
├── qabot.py
├── README.md
├── requirements.txt
└── simple_llm.py
```

### File Descriptions

- **`qabot.py`**: The main Streamlit application for the RAG-based question-answering bot.
- **`simple_llm.py`**: A simple script to test the connection to the Google Generative AI model.
- **`requirements.txt`**: A list of all the Python packages required to run the project.
- **`.gitignore`**: Specifies which files and directories to ignore for version control.
- **`my_env/`**: The Python virtual environment directory (not tracked by git).

## Setup and Installation

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd RAG-demo
```

### 2. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

**Create the environment:**
```bash
pip install virtualenv
virtualenv my_env
```

**Activate the environment (for Windows):**
```bash
my_env\Scripts\activate.bat
```

### 3. Install Dependencies

Install all the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 4. Configure Google API Key

This application requires a Google API key with access to the Generative AI models (e.g., Gemini). You need to set this key as an environment variable.

Create a `.env` file in the project root:
```
GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

The application will load this key automatically.

## How to Run the Application

Once you have completed the setup and installation steps, you can run the Streamlit application:

```bash
streamlit run qabot.py
```

This will start the application, and you can access it in your web browser at the local URL provided by Streamlit (usually `http://localhost:8501`).

## Usage

1.  **Run the app**: Use the `streamlit run` command as shown above.
2.  **Upload a PDF**: Use the file uploader in the sidebar to upload a PDF document.
3.  **Ask a Question**: Once the document is processed, type your question into the input box and press Enter.
4.  **Get the Answer**: The model will generate an answer based on the content of the PDF.

---
Readme created by AI.
