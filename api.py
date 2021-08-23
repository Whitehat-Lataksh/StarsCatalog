from flask import Flask, request, jsonify
from Data import data



app = Flask(__name__)

@app.route('/')

def main():
    return jsonify({
        'data' : data,
        'message'  :'success'
    }), 200


if __name__ == "__main__":
    app.run()
