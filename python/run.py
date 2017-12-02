#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page"

def func_for_face(f):
    #print f
    return "1"

@app.route('/facerecognize', methods=['POST'])
def index1():
    #print request.json
    a = func_for_face(request.json["photourl"])
    return jsonify({'id': a}), 201

if __name__ == '__main__':
    app.run(debug=True)
