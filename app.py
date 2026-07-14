from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host="redis", port=6379, decode_responses=True)

@app.route("/")
def home():
    count = r.incr("visitor_count")

    return f"""
    <h1>🚀 Aaditya DevOps Lab</h1>
    <h2>Docker Compose + Redis</h2>
    <h3>Visitor Count: {count}</h3>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
