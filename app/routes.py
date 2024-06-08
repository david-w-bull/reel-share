from flask import request, jsonify
from . import create_app

app = create_app()

@app.route('/get', methods=['GET'])
def get_endpoint():
    return jsonify({"message": "This is a GET endpoint"})

@app.route('/post', methods=['POST'])
def post_endpoint():
    data = request.json
    return jsonify({"message": "This is a POST endpoint", "data": data})
