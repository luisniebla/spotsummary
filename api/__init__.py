import openai
import pandas as pd
import requests
import tiktoken
from dotenv import dotenv_values, load_dotenv
from openai.embeddings_utils import get_embeddings
from quart import Quart, jsonify, request
# from .app import app

print(load_dotenv())
config = dotenv_values('.env')


openai.api_key = config['OPENAI_SECRET']


# embedding model parameters
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191

