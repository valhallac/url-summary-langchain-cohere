## URL Summarization with Langchain, Cohere LLM, and Streamlit Web App

This project generates summaries for content from a provided URL, supporting both websites and YouTube videos. It utilizes the Langchain library for text extraction, the Cohere LLM for summarization, and Streamlit for creating a user-friendly web app.

<img width="1456" alt="image" src="https://github.com/valhallac/url-summary-langchain-cohere/assets/16238095/8c73e9cc-7ecb-4989-83fb-56cf8b4b310d">



**Inspiration:**

This script is a modified version of the code found in the Langchain examples repository: [https://github.com/alphasecio/langchain-text-summarizer](https://github.com/alphasecio/langchain-text-summarizer)

**Requirements:**

* Python 3.x
* Dependencies listed in `url-summarization-requirements.txt` (installable with `pip install -r url-summarization-requirements.txt`)
* `libmagic` (install with `brew install libmagic` on macOS)

**Getting Started:**

1. **Install Dependencies:**
   ```bash
   pip install -r url-summarization-requirements.txt
   brew install libmagic  # macOS only
   ```

2. **Obtain Cohere API Key:**
   - Create a Cohere account at [https://cohere.com/](https://cohere.com/)
   - Generate an API key from your account settings.

**Running the Web App:**

1. Navigate to the directory containing the script (`url-summarization.py`).
2. Run the script using Streamlit:
   ```bash
   streamlit run url-summarization.py
   ```
   This will launch the web app in your default browser.

**Using the Web App:**

The web app will display a text box where you can enter the URL you want to summarize and add API key. Click the "Summarize" button to generate a summary of the content at the entered URL.

**Notes:**

* This script relies on external APIs (Langchain and Cohere) which may have usage limits or require paid subscriptions.
* The quality of the summaries will depend on the quality of the content extracted from the URL.

**Contributing:**

Contributions to this project are welcome! Feel free to fork the repository and submit pull requests with improvements or bug fixes.
