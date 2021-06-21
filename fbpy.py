from firebase import firebase
import time
import csv
from datetime import datetime

data = ""
firebase = firebase.FirebaseApplication('PutYourFirebaseURLHere', None)
tglf = str(datetime.now().strftime('%Y-%m-%d@%H-%M-%S'))
with open(tglf+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["WAKTU","IKAN","STATUS","STOP","HEAT","TEMP"])

while True:
    now = datetime.now()
    waktu = now.strftime("%H:%M:%S")
    ikan = str(firebase.get('/DATA/ikan/', ''))  #yourdbchild
    status = str(firebase.get('/DATA/status/', '')) #yourdbchild
    stoprq = str(firebase.get('/DATA/stop/', '')) #yourdbchild
    heater = str(firebase.get('/DATA/heater/', '')) #yourdbchild
    temp = str(firebase.get('/DATA/temp/', '')) #yourdbchild
    with open(tglf+'.csv', 'a', newline='') as f:
        f.write(waktu+','+ikan+','+status+','+stoprq+','+heater+','+temp+',\n')
    print(waktu)
    print(ikan)
    print(status)
    print(stoprq)
    print(temp) 
    print("/")
    time.sleep(120) #repeat loop in 2min
