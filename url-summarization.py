
import validators, streamlit as st
import os
from langchain_community.llms import Cohere
from langchain_core.messages import HumanMessage
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain.chains.summarize import load_summarize_chain
from langchain_core.prompts import PromptTemplate
# Streamlit app
st.subheader('Summarize URL')

# Get Cohere API key and URL to be summarized
with st.sidebar:
    os.environ["COHERE_API_KEY"] = st.text_input("Cohere API key", value="", type="password")
    st.caption("*If you don't have an Cohere API key, get it [here](https://dashboard.cohere.com/api-keys).*")
    model = st.selectbox("Cohere chat model", ("command",))
    st.caption("*If the article is long, choose another model*")
url = st.text_input("URL", label_visibility="collapsed")

# If 'Summarize' button is clicked
if st.button("Summarize"):
    # Validate inputs
    if not os.environ["COHERE_API_KEY"].strip() or not url.strip():
        st.error("Please provide the missing fields.")
    elif not validators.url(url):
        st.error("Please enter a valid URL.")
    else:
        try:
            with st.spinner("Please wait..."):
                # Load URL data
                if "youtube.com" in url:
                    loader = YoutubeLoader.from_youtube_url(url, add_video_info=True)
                else:
                    loader = UnstructuredURLLoader(urls=[url], ssl_verify=False, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                data = loader.load()

                # Initialize the Cohere module, load and run the summarize chain
                model = Cohere(model=model, temperature=0.75)
                prompt_template = """Write a short summary in 200-250 words of the following in bullet points:

                    {text}

                """
                prompt = PromptTemplate.from_template(prompt_template)
                chain = prompt | model

                summary = chain.invoke({"text": data})

                st.success(summary)
        except Exception as e:
            st.exception(f"Exception: {e}")