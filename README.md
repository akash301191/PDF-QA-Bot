# PDF QA Bot

PDF QA Bot is a user-friendly Streamlit application that lets you upload a PDF file, have a conversation with a bot about its content, and download a transcript of your conversation. Powered by the [Embedchain](https://github.com/embedchain/embedchain) library and OpenAI's GPT, this tool makes it simple to interact with your PDF documents using natural language.

## Folder Structure

```
PDF-QA-Bot/
├── pdf-qa-bot.py
├── README.md
└── requirements.txt
```

- **pdf-qa-bot.py**: The main Streamlit application.
- **requirements.txt**: A list of all required Python packages.
- **README.md**: This documentation file.

## Features

- **PDF Upload:** Easily upload any PDF file to create a knowledge base.
- **Conversational Q&A:** Ask multiple questions about the PDF content and receive answers in real time.
- **Transcript Download:** Save your entire conversation as a text file.
- **Streamlined Interface:** A clean and simple interface built with Streamlit.

## Prerequisites

- Python 3.11 or higher
- An OpenAI API key (get yours [here](https://platform.openai.com/account/api-keys))

## Installation

1. **Clone the repository** (or download it):
   ```bash
   git clone https://github.com/akash301191/pdf-qa-bot.git
   cd pdf-qa-bot
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # or
   venv\Scripts\activate           # On Windows
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run pdf-qa-bot.py
   ```
2. **Open your browser** to the local URL shown in the terminal (usually `http://localhost:8501`).
3. **Interact with the app**:
   - Enter your OpenAI API key when prompted.
   - Upload a PDF file.
   - Ask questions about the PDF content.
   - Download the transcript of your conversation if needed.

## Code Overview

- **`create_embedchain_bot`**: Initializes the Embedchain bot with OpenAI and Chroma vector database.
- **`upload_pdf_and_add_to_bot`**: Handles PDF file uploads, stores them temporarily, and adds them to the knowledge base.
- **`ask_question`**: Manages the user’s input, queries the bot, and displays the answer. It also appends Q&A pairs to a transcript stored in Streamlit’s session state.
- **`download_transcript`**: Generates a downloadable text file of the entire Q&A session.
- **`main`**: Orchestrates the Streamlit app layout, capturing the OpenAI API key, handling PDF uploads, and providing the Q&A interface.

## Contributions

Contributions are welcome! Feel free to fork the repository, make improvements, and open a pull request. Please ensure your changes follow the existing style and include any necessary documentation or tests.

