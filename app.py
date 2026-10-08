import os
import redis
from flask import Flask

app = Flask(__name__)

cache = redis.from_url(os.getenv("REDIS_URL"))


@app.route("/")
def home():
    count = cache.incr("hits")
    return f"Hello from my DevOps final project! Visits so far: {count}\n"


@app.route("/health")
def health():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
