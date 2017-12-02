#!flask/bin/python
from flask import Flask, jsonify, request
from face_detect import FaceDetect

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
    imgURL = request.json["photourl"]
    print("URL : " + imgURL)
    p = FaceDetect(imgURL)
    a = p.detect()
    return jsonify({'id': a}), 201

if __name__ == '__main__':
    app.run(debug=True)