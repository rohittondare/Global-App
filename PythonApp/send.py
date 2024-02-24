import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred = credentials.Certificate("firebase_cred.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':'https://global-test-519b0.firebaseio.com/'
})

ref = db.reference('/material')

#ref.set({

 #   'Dr Fix It':
  #  {
   #     'Fast flex 22':0
    #}
#})

with open('Material.json','r') as filee:
    data = json.load(filee)

ref.set(data)


