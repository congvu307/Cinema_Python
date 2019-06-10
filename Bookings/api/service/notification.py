from urllib import request
import json


def send_noti(noti):
    data = json.dumps(noti)
    data = str(data)
    data = data.encode('utf-8')
    req = request.Request(
        'http://localhost:8000/api/notification/add', data=data)

    # this will make the method "POST"

    resp = request.urlopen(req)
    res_string = resp.read().decode('utf-8')
    json_obj = json.loads(res_string)   
    return json_obj
