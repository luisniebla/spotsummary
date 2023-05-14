from quart import Quart, request

app = Quart(__name__)

def run() -> None:
    app.run()

@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}

app.run()