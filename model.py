import os
import numpy as np
from PIL import Image
import pytesseract


def get_info(rawimg):
    return parse_data(get_strings(rawimg))

def get_strings(rawimg):
    oem = 3
    psm = 11

    img = Image.fromarray(rawimg)
    text = pytesseract.image_to_string(img, lang='eng')
    print(text)
    texts = text.split('\n')#[0:-1]
    print(texts)
    return texts

def parse_data(texts):
    id_lst = ['id:','id :', 'id-', 'id -', 'id', 
            'ID:', 'ID :', 'ID-', 'ID -', 'ID']
    pw_lst = ['pw:', 'pw :', 'pw-', 'pw -', 'pw',
            'PW:', 'PW :', 'PW-', 'PW -', 'PW',
            'Password:', 'Password :', 'Password-', 'Password -', 'Password', 
            'password:', 'password :', 'password-', 'password -', 'password',
            'PASSWORD:', 'PASSWORD :', 'PASSWORD-', 'PASSWORD -', 'PASSWORD']


    wifi = dict()
    wifi['id'] = None
    wifi['pw'] = None
    for text in texts:
        text = text.strip()
        for id_ in id_lst:
            if text.startswith(id_):
                text = text[text.find(id_) + len(id_):]
                wifi['id'] = text.strip()
        for pw_ in pw_lst:
            if text.startswith(pw_):
                text = text[text.find(pw_) + len(pw_):]
                wifi['pw'] = text.strip()

    if wifi['id'] == None or wifi['pw'] == None:
        wifi['id'] = 'INVALID'
        wifi['pw'] = 'INVALID'

    return wifi

def preprocess(img_path):
    img = Image.open(os.getcwd()+img_path)
    imgarr = np.array(img)
    print(imgarr.shape)
    return imgarr


if __name__ == '__main__':
    img_path = '/data/0.jpg'
    rawimg = preprocess(img_path)
    print(get_info(rawimg))
