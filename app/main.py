from flask import Flask, request, jsonify
import redis
import os

app = Flask(__name__)
r = redis.Redis(host=os.environ.get("REDIS_HOST", "localhost"), port=6379, db=0)

@app.route('/add', methods=['POST'])
def add_data():
    key = request.json['key']
    value = request.json['value']
    r.set(key, value)
    return jsonify({"status": "ok"})

@app.route('/get/<key>', methods=['GET'])
def get_data(key):
    value = r.get(key)
    if value is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify({key: value.decode()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
