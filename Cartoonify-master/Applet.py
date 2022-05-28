import requests
import json
import io
from os import path
import time
from PIL import Image
import cv2
def sendToServer(filename):
    config={}
    config["Brightness"]=float(input("How much do you want to increase brightness:"))
    config["Contrast"]=float(input("How much do you want to increase contrast:"))
    config["Edgify"]=int(input("Do you want to edgify the image(1:Yes/0:No):"))
    config["Monocle"]=int(input("Do you want to add a monocle(1:Yes/0:No):"))
    config["EyePatch"]=int(input("Do you want to add an eyepatch(1:Yes/0:No):"))
    config["Moustache"]=int(input("Do you want to add a Moustache(1:Yes/0:No):"))

    url="http://localhost:8080/"
    data = config
    files = [
        ('image', (filename, open(filename, 'rb'), 'application/octet')),
        ('data', ('data', json.dumps(data), 'application/json')),
    ]
    r = requests.post(url,files=files)

    image_bytes = io.BytesIO(r.content)
    img = Image.open(image_bytes)
    img.show()
    sv=int(input("Do you want to save this picture?(0:No,1:Yes)"))
    if(sv==1):
        if(path.exists("Cartoon_Image.jpg")==False):
            img.save("Cartoon_Image.jpg")
        else:
            i=1
            while True:
                save_str="Cartoon_Image[{num}].jpg".format(num=i)
                if(path.exists(save_str)):
                    i=i+1
                    continue
                else:
                    img.save(save_str)
                    break

def Webcam():
    webcm=int(input("What webcam do you want to use(Integers only):"))
    cap=cv2.VideoCapture(webcm, cv2.CAP_DSHOW)    
    
    startTime=0
    font=cv2.FONT_HERSHEY_COMPLEX
    while(True):
        ret,frame=cap.read()
        height=int(cap.get(4))
        width=int(cap.get(3))
        if(ret==False):
            print("Webcam error")
            break
        time1=time.time()
        if(startTime==0):
            cv2.putText(frame,'C:Click Image',(10,height-10),font,0.75,(0,0,0),2,cv2.LINE_AA)
            cv2.putText(frame,'Q:Exit',(width-100,height-10),font,0.75,(0,0,0),2,cv2.LINE_AA)
        if(startTime!=0):
            if(time1-startTime>=6):
                cv2.imwrite("image.jpg",frame)
                cv2.destroyAllWindows() 
                sendToServer("image.jpg")
                break
            else:
                k=6-int(time1-startTime)
                
                cv2.putText(frame,str(k),(10,height-10),font,2,(0,0,0),3,cv2.LINE_AA)
        
        
        cv2.imshow("frame",frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break
        if k==ord('c'):
            startTime=time.time()
    cap.release()

def UploadSave():
    filename=input("Enter the name of the file(Should be in this folder and specify the file type):")
    sendToServer(filename)

typ=int(input("Enter 1 for uploading an image in PC, 2 for uploading through webcam"))
if(typ==1):
    UploadSave()
elif(typ==2):
    Webcam()




    

cv2.destroyAllWindows()



