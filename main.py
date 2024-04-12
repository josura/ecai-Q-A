## program that uses langchain to send Q&A to OpenAI's GPT-3

# Imports
import os
from dotenv import load_dotenv,find_dotenv
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_openai import ChatOpenAI


load_dotenv(find_dotenv())


# Set API keys and the models to use
model_id = "gpt-3.5-turbo"

OpenAI_key = os.environ.get("OPEN_AI_KEY")

# Define the LLM we plan to use. Here we are going to use ChatGPT 3.5 turbo
llm=ChatOpenAI(model_name = model_id, temperature=0.2, max_tokens=100, api_key=OpenAI_key)

# Define the document loader
document_loader = TextLoader()
# pdf loader
pdf_loader = PyPDFLoader()

# Define the index creator
index_creator = VectorstoreIndexCreator()