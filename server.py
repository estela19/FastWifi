import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return("Anybody here?")

@app.route('/ocr_image/', methods=['POST'])
def get_img():
    data  = request.files['file'].read()
    jpg_arr = np.frombuffer(data, dtype=np.unit8)
    img = cv2.imdecode(jpg_arr, cv2.IMREAD_COLOR)
    print(img.shape)
    # TODO: predict

    return jsonify({'id':'test_wifi', 'pw':'a12345'}) 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10301)
