import cv2
import os

def get_img_bytes(img_path):
    img = cv2.imread(os.getcwd()+img_path, cv2.IMREAD_COLOR)
    img_bytes = cv2.imencode('.jpg', img)[1].tobytes()
    return img_bytes

if __name__ == '__main__':
    f = open('test_binary', 'wb')
    f.write(get_img_bytes('/data/0.jpg'))
    f.close()
