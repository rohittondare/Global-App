import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json

cred = credentials.Certificate("firebase_cred.json")
firebase_admin.initialize_app(cred,{

    'databaseURL':'https://global-test-519b0.firebaseio.com/'
})

ref = db.reference('/users')
result = ref.get()

dictt = dict(result)

#print(dictt)
# Files for saving data from firebase
Emp_Master_csv = "emp_master.csv"
Material_csv = "material.csv"
Engineer_csv = "engineer.csv"

with open(Emp_Master_csv, 'w') as f:
    f.write("\n")
    f.write("UserID,Username,Approved,Name,Password,Gender,DOB,Blood Group,Residence Number,Mobile1,Mobile2,Permanent Address,Permanent City,Permanent State,Permanent PIN,Temp Address,Temp City,Temp State,Temp PIN,Doctor Name,Doctor Number,Emergency Contact Name,Emergency Contact Number,PAN Number,Aadaar Number,Account Number,Account Type,Bank Address,IFSC Code,Bank Number\n")
    for key in dictt.keys():
        f.write("%s," % (key))
        data1 = dictt[key]
        f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (data1['username'],data1['approve'],data1['Name'], data1['password'],data1['Gender'],data1['DOB'],data1['Blood Group'],data1['Residence Number'],data1['Mobile Number 1'], data1['Mobile Number 2'], data1['Permanent Address'], data1['Permanent City'], data1['Permanent State'], data1['Permanent PIN'], data1['Temporary Address'], data1['Temporary City'], data1['Temporary State'], data1['Temporary PIN'], data1['Doctor Name'], data1['Doctor Number'], data1['Emergency Contact Name'], data1['Emergency Contact Number'], data1['PAN Number'], data1['Aadhaar Number'], data1['Account Number'], data1['Account Type'], data1['Bank Address'], data1['IFSC Code'], data1['Bank Number'] ))
f.close()
#print(data1)


ref_sites = db.reference('/sites')
dict_sites = ref_sites.get()
arr_keys = dict_sites.keys()

with open(Engineer_csv, 'w') as engineer_file:
    engineer_file.write("\n")
    engineer_file.write("Site,Username,IN Date,IN Time,IN Address,IN Latitute, IN Longitude,OUT Date,OUT Time,OUT Address,OUT Latitute,OUT Longitude\n")
    for p_id, p_info in dict_sites.items():
        print("\nSite:", p_id)
        
        for key in p_info:
            #print(key + "q:q",p_info[key])
            temp_dict = p_info[key]
            #print(key + "..Q..", temp_dict)
            if(key == "Material"):
                print(key)
                with open(Material_csv, 'w') as material_file:
                    material_file.write("\n")
                    #material_file.write("UserID,Username,Approved,Name,Password,Gender,DOB,Blood Group,Residence Number,Mobile1,Mobile2,Permanent Address,Permanent City,Permanent State,Permanent PIN,Temp Address,Temp City,Temp State,Temp PIN,Doctor Name,Doctor Number,Emergency Contact Name,Emergency Contact Number,PAN Number,Aadaar Number,Account Number,Account Type,Bank Address,IFSC Code,Bank Number\n")
                    for temp in temp_dict.keys():
                        material_file.write("%s,%s" % (temp,p_id))
                        #data1 = dictt[temp]
                        #material_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" % (data1['username'],data1['approve'],data1['Name'], data1['password'],data1['Gender'],data1['DOB'],data1['Blood Group'],data1['Residence Number'],data1['Mobile Number 1'], data1['Mobile Number 2'], data1['Permanent Address'], data1['Permanent City'], data1['Permanent State'], data1['Permanent PIN'], data1['Temporary Address'], data1['Temporary City'], data1['Temporary State'], data1['Temporary PIN'], data1['Doctor Name'], data1['Doctor Number'], data1['Emergency Contact Name'], data1['Emergency Contact Number'], data1['PAN Number'], data1['Aadhaar Number'], data1['Account Number'], data1['Account Type'], data1['Bank Address'], data1['IFSC Code'], data1['Bank Number'] ))
                material_file.close()
            if(key == "engineers"):
                print(key)
                #with open(Engineer_csv, 'a') as engineer_file:
                engineer_file.write("\n")
                #engineer_file.write("Username,IN Date,IN Time,IN Address,IN Latitute, IN Longitude,OUT Date,OUT Time,OUT Address,OUT Latitute,OUT Longitude\n")
                for user in temp_dict.keys():
                    engineer_file.write("\n%s,%s," % (p_id,user))
                    data11 = temp_dict[user]
                    #print(data11)
                    for data in data11.keys():
                        #print(data)
                        tempp = data11[data]
                        #print(tempp)
                        if(data == 'IN'):
                            in_add = tempp['IN_Address']
                            in_add = in_add.replace(',','')
                            #print(in_add)
                            engineer_file.write("%s,%s,%s,%s,%s," % (tempp['Date'],tempp['IN_time'],in_add,tempp['IN_Latitude'],tempp['IN_Longitude']))
                        if(data == 'OUT'):
                            out_add = tempp['OUT_Address']
                            out_add = in_add.replace(',','')                            
                            engineer_file.write("%s,%s,%s,%s,%s\n" % (tempp['Date'],tempp['OUT_time'],out_add,tempp['OUT_Latitude'],tempp['OUT_Longitude']))

                #engineer_file.close()


