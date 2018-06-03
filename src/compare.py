#coding=utf8  
import cv2  
import cv2.cv as cv  
import requests  
import json  
   
##capture = cv.CaptureFromCAM(0)                
    
##while True:    
##    img = cv.QueryFrame(capture)  
##    cv.ShowImage("camera",img)    
##    key = cv.WaitKey(10)    
##    if key == 27:    
##        break    
##    if key == ord(' '):     
##        filename = "face.jpg"    
##        cv.SaveImage(filename,img)  
##        print "Image captured"  
##          
##del(capture)   
##cv.DestroyWindow("camera")  
   
url = 'https://api-cn.faceplusplus.com/facepp/v3/search'  
payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
           'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',  
           'faceset_token':'eb024da205cc53a590407bc7247567d6',  
           }  
files = {'image_file':open('2.jpg', 'rb')}  
r = requests.post(url,files=files,data=payload)  
data=json.loads(r.text)  
print r.text  
if data["results"][0]["face_token"] == "e98868958599254b6d3994a055c4af3e" and data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:  
    print'\n This guy is Trump, attendence is confirmed.'
elif data["results"][0]["face_token"] == "bdc26225e7ad977aef284f0db46bc6e2" and data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:  
    print'\n This guy is Pudding, attendence is confirmed.'  
else:  
    print '\n Not a member of SE26.'
width = data['faces'][0]['face_rectangle']['width']  
top = data['faces'][0]['face_rectangle']['top']  
height = data['faces'][0]['face_rectangle']['height']  
left = data['faces'][0]['face_rectangle']['left']  
   
img = cv2.imread("2.jpg")  
vis = img.copy()  
cv2.rectangle(vis, (left, top), (left+width, top+height),(0, 255, 0), 2)  
cv2.imshow("Image", vis)  
cv2.waitKey (0)  
