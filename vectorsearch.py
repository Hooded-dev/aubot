from links import links
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import FAISS
import os
import openai
import requests
from bs4 import BeautifulSoup
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA
from langchain.text_splitter import CharacterTextSplitter
from langchain import OpenAI
import tiktoken
import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import pickle
from langchain.document_loaders import WebBaseLoader,OnlinePDFLoader
urls_list = links()
def load_and_split(urls):
    loader = WebBaseLoader(urls)
    scrape_data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter (chunk_size=1000, chunk_overlap=200)
    texts_from_links = text_splitter.split_documents(scrape_data)
    print(len(texts_from_links))
    return texts_from_links

def links_embed(texts_from_links):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(texts_from_links, embeddings)
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)
    return vectorstore

def add_pdf(vectorstore):
    loader = OnlinePDFLoader("https://au.edu.pk/AU_Documents/Details_of_Dept_Program_Representatives_for_Admissions%20Fall_2022.pdf")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter (chunk_size=1000, chunk_overlap=200)
    texts_from_pdf_link = text_splitter.split_documents(data)
    embeddings = OpenAIEmbeddings()
    vectorstore_added = FAISS.from_documents(texts_from_pdf_link, embeddings)
    vectorstore.merge_from(vectorstore_added)
    print('working')
    return vectorstore

url_list = load_and_split(urls_list)
db = links_embed(url_list)
add_pdf(db)