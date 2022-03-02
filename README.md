# FastWifi
Get wifi ID/PW from wifi information image by OCR. In this repo, ocr server which parsing wifi ID/PW. Now you can parse english only

## Key Feature
![struct](https://github.com/estela19/FastWifi/blob/master/utils/structure.png)  

* take a photo including wifi id/pw (application)
* get wifi id/pw from photo (server)
* make QRcode able to connect wifi directly (application)  
you can see applications at below related application

## Server protocol
### client to server
image data (byte stream)
### server to client
json format id/pw pair  
```{'id': 'testwifi', 'pw': 'a12345'}```

if can't found valid id/pw, return INVALID  
```{'id': 'INVALID', 'pw': 'INVALID'}```

## Development info
* Language : python 3.8
* Environment : Linux
* Library : Flask, pytesseract
* period : 2022.02.28.

## Quick Start
prerequest: conda  
you should change your server ip & port in configs.py
```
git clone https://github.com/estela19/FastWifi
cd FastWifi
conda env create -n FastWifi -f environment.yaml
conda activate FastWifi
python server.py
```


## Related Application
wifi connector application using Flutter
* [wifi_ocr](https://github.com/GiveMeMandu/wifi_ocr) by [woochan kim](https://github.com/GiveMeMandu), [hyunsu kim](https://github.com/1cekrim)  
![h0](https://github.com/estela19/FastWifi/blob/master/utils/h0.png)  
![h1](https://github.com/estela19/FastWifi/blob/master/utils/h1.png)
* [wifi-is-auto](https://github.com/you4rin/wifi-is-auto/tree/develop) by [seokwon moon](https://github.com/you4rin), [seonghwan kim](https://github.com/FYLSunghwan)
* [WifiConnector](https://github.com/frechele/WifiConnector) by [junyeong park](https://github.com/frechele), [kyounguk chae](https://github.com/ShyRoute)
![j0](https://github.com/estela19/FastWifi/blob/master/utils/j0.png)  
![j1](https://github.com/estela19/FastWifi/blob/master/utils/j1.png)  
![j2](https://github.com/estela19/FastWifi/blob/master/utils/j2.png)
