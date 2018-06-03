import cv2  
import requests  
import json  

img_name = '2'
   
urlDetect = 'https://api-cn.faceplusplus.com/facepp/v3/detect'  
files = {'image_file':open('../camera/'+ img_name +'.jpg', 'rb')}  
payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
           'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',  
           'return_landmark': 0,  
           'return_attributes':'gender,age,glass'}  
   
r = requests.post(urlDetect,files=files,data=payload)  
data=json.loads(r.text)  
print r.text  
width = data['faces'][0]['face_rectangle']['width']  
top = data['faces'][0]['face_rectangle']['top']  
height = data['faces'][0]['face_rectangle']['height']  
left = data['faces'][0]['face_rectangle']['left']  
faceToken = data['faces'][0]['face_token']
 
img = cv2.imread("../camera/2.jpg")  
vis = img.copy()  
cv2.rectangle(vis, (left, top), (left+width, top+height),(0, 255, 0), 2)  
cv2.imshow("Image", vis)  
cv2.waitKey (0)  

urlCreate = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'  
payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
           'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',  
           'display_name':'Class SE26 parttime',  
           'outer_id':'SE26',  
           'face_tokens':faceToken,
           'force_merge':1
           }  
r = requests.post(urlCreate,data=payload)  
print r.text  
