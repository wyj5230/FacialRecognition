import picamera
import time
from upload_image import Upload
from detect import Detect
import cv2  
import cv2.cv as cv  
import requests  
import json  

def CaptureImage(img_name, event_flag):
    camera = picamera.PiCamera()
	face_set = 'SE26'
    if img_name == '':
        img_file_name = 'student_image.jpg'
        img_name = 'student_image'
    else:
        img_file_name = img_name + '.jpg'
    img_path = '../camera/' + img_file_name
    try:
        camera.start_preview()
        time.sleep(5)
        camera.capture(img_path)
    finally:
        camera.stop_preview()
        camera.close()

    if(event_flag == 'EntryForm'):
        face_token = DetectFace(img_path)
        if face_token != 'ERR_NO_FACE':
            Upload(img_path, img_name)
			AddFaceTokenToFaceCet(face_token, face_set)
        return face_token
    else:
        RecogniseFace(img_path, face_set)

def DetectFace(img_path):
    face_token = Detect(img_path)
    print face_token
    return face_token

def AddFaceTokenToFaceCet(face_token, face_set)
	url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'  
	payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
           'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',  
           'display_name':'Class SE26 parttime',  
           'outer_id':face_set,  
           'face_tokens':face_token,
           'force_merge':1
           }  
	r = requests.post(url,data=payload)  
	print r.text  

	
def RecogniseFace(img_path, face_set):
	url = 'https://api-cn.faceplusplus.com/facepp/v3/search'  
	payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
			   'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',
			   'image_url':img_path,
			   'outer_id':face_set,  
			   }  
	r = requests.post(url,data=payload)  
	data=json.loads(r.text)  
	print r.text  
	if len(data['results']) < 1:
		print '\n No face found in the image.'
        return 'ERR_NO_FACE'
	if data["results"][0]["confidence"]>=data["thresholds"]["1e-5"]:  
		print 'Student found! Face_token = ' + data["results"][0]["face_token"]
	else:  
		print '\n Not a member of SE26.'
		
	width = data['faces'][0]['face_rectangle']['width']  
	top = data['faces'][0]['face_rectangle']['top']  
	height = data['faces'][0]['face_rectangle']['height']  
	left = data['faces'][0]['face_rectangle']['left']  
	   
	img = cv2.imread(img_path)  
	vis = img.copy()  
	cv2.rectangle(vis, (left, top), (left+width, top+height),(0, 255, 0), 2)  
	cv2.imshow("Image", vis)  
	cv2.waitKey (0)  
	return data["results"][0]["face_token"]









    
