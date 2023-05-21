import requests
from dotenv import dotenv_values, load_dotenv
from quart import Quart, request

app = Quart(__name__)
app.config.from_prefixed_env()
print(load_dotenv())
config = dotenv_values('.env')

def run() -> None:
    app.run()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/embeddings")
async def embeddings():
    json = await request.get_json()
    print(json)
    resp = requests.post(
        'https://api.openai.com/v1/embeddings',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {config["OPENAI_SECRET"]}'
        },
        json={
            'input': 'Hello World',
            'model': 'text-embedding-ada-002'
        },
    )
    return resp.json()


@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}

app.run()