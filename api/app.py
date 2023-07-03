from quart import Quart, jsonify, request
from quart_cors import cors

app = Quart(__name__)
app.config.from_prefixed_env()
app = cors(app, allow_origin="http://localhost:3000")
