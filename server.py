import json
import cv2
import numpy as np
from flask import Flask, request, jsonify

from model import get_info
from configs import SEVER_CONFIGS

app = Flask(__name__)
server_configs = SEVER_CONFIGS()

@app.route('/')
def hello():
    return("Anybody here?")

@app.route('/ocr_image/', methods=['POST'])
def get_img():
    data  = request.get_data()
    jpg_arr = np.frombuffer(data, dtype=np.uint8)
    img = cv2.imdecode(jpg_arr, cv2.IMREAD_COLOR)
    if img is None:
        return jsonify({'id':'INVALID', 'pw':'INVALID'})
    info = get_info(img)    
    print(info)
    return jsonify(info) 

if __name__ == '__main__':
    app.run(host=server_configs.ip, port=server_configs.port)
