import openai
import pandas as pd
import requests
import tiktoken
from dotenv import dotenv_values, load_dotenv
from openai.embeddings_utils import get_embeddings
from quart import Quart, request

app = Quart(__name__)
app.config.from_prefixed_env()
print(load_dotenv())
config = dotenv_values('.env')


openai.api_key = config['OPENAI_SECRET']


def run() -> None:
    app.run()


# embedding model parameters
embedding_model = "text-embedding-ada-002"
embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
max_tokens = 8000  # the maximum for text-embedding-ada-002 is 8191


@app.post("/embeddings")
async def embeddings():
    input_datapath = 'api/data/Reviews.csv'
    df = pd.read_csv(input_datapath, index_col=0)
    df = df[['Time', 'ProductId', 'UserId', 'Score', 'Summary', 'Text']]
    df = df.dropna()
    df.head(2)

    # subsample to 1k more recent reviews
    top_n = 1000
    df = df.sort_values(by='Time', ascending=False).tail(top_n * 2)
    df.drop('Time', axis=1, inplace=True)

    encoding = tiktoken.get_encoding(embedding_encoding)

    # omit long reviews
    df['n_tokens'] = df.Text.apply(lambda x: len(encoding.encode(x)))
    df = df[df.n_tokens <= max_tokens].tail(top_n)

    # get embeddings
    df['embedding'] = df.Text.apply(lambda x: get_embeddings(x, embedding_model))
    df.to_csv('data/reviews_embeddings.csv')
    return str(len(df))
    # return str(df)


@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}


@app.get("/health")
async def health():
    return {"status": "ok"}


app.run()
