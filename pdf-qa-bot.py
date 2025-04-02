import base64, os, tempfile
import streamlit as st
from embedchain import App

def create_embedchain_bot(db_path: str, api_key: str) -> App:
    """
    Initialize the embedchain bot with the given database path and OpenAI API key.
    """
    config = {
        "llm": {"provider": "openai", "config": {"api_key": api_key}},
        "vectordb": {"provider": "chroma", "config": {"dir": db_path}},
        "embedder": {"provider": "openai", "config": {"api_key": api_key}}
    }
    return App.from_config(config=config)


def upload_pdf_and_add_to_bot(app: App) -> bool:
    """
    Prompts the user to upload a PDF file, adds it to the bot's knowledge base,
    and returns True if a PDF was uploaded.
    """
    pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
    if pdf_file:
        # Save the uploaded PDF to a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(pdf_file.getvalue())
            tmp_file_path = tmp_file.name

        # Add the PDF to the knowledge base
        app.add(tmp_file_path, data_type="pdf_file")

        # Clean up the temporary file
        os.remove(tmp_file_path)
        st.success(f"Added {pdf_file.name} to the knowledge base!")
        return True
    return False

def ask_question(app: App) -> None:
    """
    Prompts the user to ask a question about the uploaded PDF and displays the answer.
    Stores the conversation in session state.
    """
    prompt = st.text_input("Ask a question about the PDF")
    if prompt:
        answer = app.chat(prompt)
        st.write(answer)
        # Initialize transcript if not already present
        if "transcript" not in st.session_state:
            st.session_state.transcript = ""
        # Append Q&A pair to the transcript
        st.session_state.transcript += f"Query: {prompt}\nResponse: {answer}\n\n"

def download_transcript() -> None:
    """
    Provides a download button for the transcript.
    """
    transcript = st.session_state.get("transcript", "")
    if transcript:
        st.download_button(
            label="Download Transcript",
            data=transcript,
            file_name="pdf-qa-transcript.txt",
            mime="text/plain"
        )

def main() -> None:
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="PDF QA BOT")

    # Inject custom CSS for wider margins
    st.markdown(
        """
        <style>
        /* Increase left and right padding of the main container */
        .block-container {
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='font-size: 2.5rem;'>📚 PDF QA Bot</h1>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to PDF QA Bot — a user-friendly tool that lets you upload a PDF and ask questions about its content.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://platform.openai.com/account/api-keys)."
    )

    if not openai_api_key:
        return

    # Initialize the bot with a temporary database directory
    db_path = tempfile.mkdtemp()
    app = create_embedchain_bot(db_path, openai_api_key)

    # Handle PDF upload, summary generation, Q&A, and transcript download
    pdf_uploaded = upload_pdf_and_add_to_bot(app)
    if pdf_uploaded:
        st.markdown("<br>", unsafe_allow_html=True)
        
        ask_question(app)
        download_transcript()

if __name__ == "__main__":
    main()
