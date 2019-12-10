import requests
import json
import time
from datetime import datetime
# current date and time
now = datetime.now()
timestamp = str(int(datetime.timestamp(now)))

mainUrl = "http://localhost:8013/"
root = {}
index = 0
#create user nvvuon
url = mainUrl + "user"
data = {
    "username": "stoke_keeper"+timestamp,
    "password": "1",
    "role": "stoke_keeper"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
time.sleep(5)

# authenicationUser

url = mainUrl + "authentication"
data = {
    "username": "stoke_keeper"+timestamp,
    "password": "1"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
respond_json = json.loads(respond.text)
authorizationstoke_keeper = respond_json['authorization']
#create user nvvuon
url = mainUrl + "user"
data = {
    "username": "nurse"+timestamp,
    "password": "1",
    "role": "nurse"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
time.sleep(5)

# authenicationUser

url = mainUrl + "authentication"
data = {
    "username": "nurse"+timestamp,
    "password": "1"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
respond_json = json.loads(respond.text)
authorizationnurse = respond_json['authorization']
#create user nvvuon
url = mainUrl + "user"
data = {
    "username": "patient"+timestamp,
    "password": "1",
    "role": "patient"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
time.sleep(5)

# authenicationUser

url = mainUrl + "authentication"
data = {
    "username": "patient"+timestamp,
    "password": "1"
}
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
respond = requests.post(url, data=json.dumps(data), headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)
respond_json = json.loads(respond.text)
authorizationpatient = respond_json['authorization']


# create product
url = mainUrl + "trustion_drug/drug_import"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': authorizationpatient}
product_data = {
     "name":"string"
    }

files = {
      }
product_create_respond = requests.post(url, data=json.dumps(product_data), headers=headers, files = files)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = product_create_respond.status_code
root[index][url]['response'] = json.loads(product_create_respond.text)
product_create_respond_json = json.loads(product_create_respond.text)

productId = product_create_respond_json["id"]

url = mainUrl + "trustion_drug/get_drug"+"?"+"id="+str(productId)
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}


respond = requests.get(url, headers=headers)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)




url = mainUrl + "trustion_drug/update_status"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': authorizationpatient}

data = {
                    "id":productId
                    ,
                    "quantity":"string"
                    ,
                    "price":"string"
                    
}
files = {
      }

respond = requests.put(url, data=data, headers=headers, files=files)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)


url = mainUrl + "trustion_drug/update_location"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain', 'Authorization': authorizationpatient}

data = {
                    "id":productId
                    ,
                    "longitude":"string"
                    ,
                    "latitude":"string"
                    
}
files = {
      }

respond = requests.put(url, data=data, headers=headers, files=files)
index += 1
root[index] = {}
root[index][url] = {}
root[index][url]['status_code'] = respond.status_code
root[index][url]['response'] = json.loads(respond.text)










with open("log_script_result.json", "w") as outfile:
    json.dump(root, outfile)