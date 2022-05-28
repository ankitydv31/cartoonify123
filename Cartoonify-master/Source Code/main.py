from flask import Flask, request, send_file
from flask_cors import CORS, cross_origin
import cv2
import json
from PIL import Image
import numpy as np
from functions.AddLines import getedges
from functions.BriCon import Brightness_contrast
from functions.EyePatch import AddEyePatch
from functions.monocle import AddMonocle
from functions.moustache import AddMoustache
from functions.outline import edge
from functions.cartoon import cartoon
from functions.brightness import adjust_brightness
app=Flask("predict_car")
CORS(app, support_credentials=True)
@app.route('/',methods=["POST"])
@cross_origin(supports_credentials=True)
def CartoonifyImage():
    file=request.files['image']
    rec_img=Image.open(file.stream)
    img = cv2.cvtColor(np.array(rec_img), cv2.COLOR_RGB2BGR)
    
    k=json.load(request.files['data'])
    cartoonimg=img
    cartoonimg=Brightness_contrast(cartoonimg,k["Brightness"],k["Contrast"])
    if(k["Edgify"]==1):
        cartoonimg=getedges(cartoonimg)

    
    if(k["Monocle"]==1):
        cartoonimg=AddMonocle(cartoonimg,img)
    if(k["EyePatch"]==1):
        cartoonimg=AddEyePatch(cartoonimg,img)
    if(k["Moustache"]==1):
        cartoonimg=AddMoustache(cartoonimg,img)
        
    
    cv2.imwrite("Image.jpg",cartoonimg)
    return send_file("Image.jpg",mimetype="image/jpeg")
if __name__=='__main__':
    app.run(host="localhost",port=8080)