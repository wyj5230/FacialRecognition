import requests  
url = 'https://api-cn.faceplusplus.com/facepp/v3/faceset/create'  
payload = {'api_key': 'LcT56P9UKVzFNkNPmuU77LJTi8IMvCJ6',  
           'api_secret': 'CEQ1oWuHt_f2fgnBYQWFukUYMORj_Kcg',  
           'display_name':'Class SE26 parttime',  
           'outer_id':'SE26',  
           'face_tokens':'bdc26225e7ad977aef284f0db46bc6e2',
           'force_merge':1
           }  
r = requests.post(url,data=payload)  
print r.text  
