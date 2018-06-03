import sys, os
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
import base64


certificate_path =  '/'.join(os.path.realpath(__file__).replace('\\', '/').split('/')[:-1]) + '/certificate.json'

def Upload(img_path, img_name):
    cred = credentials.Certificate(certificate_path)
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'facerecognizationdata.appspot.com'
    })
    bucket = storage.bucket()

    with open(img_path, "rb") as image_file:
        image_data = base64.b64encode(image_file.read())
        bucket = storage.bucket()
        blob = bucket.blob(img_name + '.jpg')
        blob.upload_from_filename(
            img_path,
            content_type='image/jpg'
        )
        print(blob.public_url)
##        blob = bucket.blob(img_name + '.jpg')
##        blob.upload_from_filename(
##            image_data,
##            content_type='image/jpg'
##        )
##        print(blob.public_url)

##if __name__ == '__main__':
##
##
##    img_path = '/'.join(os.path.realpath(__file__).replace('\\', '/').split('/')[:-1]) + '/2018_student.jpg'
##
##
##    img_name = '2018_student'
##
##    ImageUploading.Upload(img_path, img_name)