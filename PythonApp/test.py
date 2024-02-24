from firebase import firebase
import csv

firebase = firebase.FirebaseApplication("https://global-test-519b0.firebaseio.com/", None)

result = firebase.get('users', '')
print("hi")
#print(result)

dictt = dict(result)
csv_columns = ['Service', 'ShowName', 'Seasons']

print(dictt)
csv_file = "data.csv"

with open('data.csv', 'w') as f:
    f.write("\n")
    f.write("UserID,Username,Approved,Name,Password,Gender,DOB,Blood Group,Residence Number,Mobile1,Mobile2,Permanent Address,Permanent City,Permanent State,Permanent PIN,Temp Address,Temp City,Temp State,Temp PIN,Doctor Name,Doctor Number,Emergency Contact Name,Emergency Contact Number,PAN Number,Aadaar Number,Account Number,Account Type,Bank Address,IFSC Code,Bank Number\n")
    for key in dictt.keys():
        f.write("%s," % (key))
        data1 = dictt[key]
        f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (data1['username'],data1['approve'],data1['Name'], data1['password'],data1['Gender'],data1['DOB'],data1['Blood Group'],data1['Residence Number'],data1['Mobile Number 1'], data1['Mobile Number 2'], data1['Permanent Address'], data1['Permanent City'], data1['Permanent State'], data1['Permanent PIN'], data1['Temporary Address'], data1['Temporary City'], data1['Temporary State'], data1['Temporary PIN'], data1['Doctor Name'], data1['Doctor Number'], data1['Emergency Contact Name'], data1['Emergency Contact Number'], data1['PAN Number'], data1['Aadhaar Number'], data1['Account Number'], data1['Account Type'], data1['Bank Address'], data1['IFSC Code'], data1['Bank Number'] ))


print(data1)