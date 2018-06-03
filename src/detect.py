import cv2  
import requests  
import json  
   
url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'  
files = {'image_file':open('2.jpg', 'rb')}  
payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
           'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',  
           'return_landmark': 0,  
           'return_attributes':'gender,age,glass'}  
   
r = requests.post(url,files=files,data=payload)  
data=json.loads(r.text)  
print r.text  
width = data['faces'][0]['face_rectangle']['width']  
top = data['faces'][0]['face_rectangle']['top']  
height = data['faces'][0]['face_rectangle']['height']  
left = data['faces'][0]['face_rectangle']['left']  
   
img = cv2.imread("2.jpg")  
vis = img.copy()  
cv2.rectangle(vis, (left, top), (left+width, top+height),(0, 255, 0), 2)  
cv2.imshow("Image", vis)  
cv2.waitKey (0)  
