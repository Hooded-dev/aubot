from links import links
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.document_loaders import SeleniumURLLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
import os
from langchain.chains import RetrievalQA
import openai
import requests
from bs4 import BeautifulSoup
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.document_loaders import WebBaseLoader
import inspect
from getpass import getpass
from langchain import OpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory,
                                                  ConversationSummaryMemory,
                                                  ConversationBufferWindowMemory,
                                                  ConversationKGMemory)
import tiktoken
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import pickle
from langchain.document_loaders import WebBaseLoader

urls_list = links()
def load_and_split(urls):
    loader = WebBaseLoader(urls)
    scrape_data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter (chunk_size=1000, chunk_overlap=200)
    texts_from_links = text_splitter.split_documents(scrape_data)
    print(len(texts_from_links))
    return len(texts_from_links)

load_and_split(urls_list)
