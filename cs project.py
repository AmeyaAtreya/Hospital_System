import csv
import os
path = "C:/Users/RIS13/Desktop"
isFile = os.path.isfile(path)
if isFile==True:
    f = open("patient.csv","r",newline = "")
    r = csv.reader(f)
else:
    f = open("patient.csv","w+",newline = "")
    r = csv.reader(f)
c = 1
for i in r:
    c+=1
f.close()
def newpatient():
    global c
    print("Add a new Patient Record")
    print("========================")
    f = open("patient.csv","a",newline = '')
    a = csv.writer(f)
    patient_id = c
    patient_name = input("Enter the Patient's name:")
    age = input("Enter age:")
    sex = input("Enter sex: M/F").upper()
    doctor_name = input("Enter the Doctor's name:")
    fee = input("Enter the fee:")
    status = "active"
    print("–––––––––––––––––––––––––––––––––––––––––––––")
    new_rec = [patient_id,patient_name,age,sex,doctor_name,fee,status]
    a.writerow(new_rec)
    f.close()
    c+=1
    print("Patient record saved")
def editpatient():
    print("Modify a Patient's Record")
    print("=======================")
    f = open("patient.csv","r",newline = "")
    f1 = open("temp.csv","w",newline = "")
    s = input("Enter the Patient name whose record you want to modify:")
    r = csv.reader(f)
    w = csv.writer(f1)
    found = 0
    for i in r:
        if i[1]==s:
            found = 1
            if i[6]=="active":
                print("———————————————————————————————————————")
                print("Patient's id :",i[0])
                print("Patient's name :",i[1])
                print("Patient's age :",i[2])
                print("Patient's sex :",i[3])
                print("Name of Doctor :",i[4])
                print("Fee :",i[5])
                print("————————————————————————————————————————")
                choice = input("Do you want to modify this Patient's record?\n(Y/N)").lower()
                if choice=="y":
                    print("————————————————————————————————————")
                    patient_id = i[0]
                    patient_name = input("Enter new Patient's name:")
                    age = input("Enter Age:")
                    sex = input("Enter sex(M/F):")
                    doctor_name = input("Enter Doctor's name:") 
                    fee = input("Enter fee:")
                    status = "active"
                    print("————————————————————————————————————")
                    i = [patient_id,patient_name,age,sex,doctor_name,fee,status]
                    w.writerow(i)
                    print("Patient record modified")
                else:
                    w.writerow(i)
            else:
                print("Patient is already discharged")
                choice = input("Do you want to modify this Patient's record?\n(Y/N)").lower()
                if choice=="y":
                    patient_id = i[0]
                    patient_name = i[1]
                    age = i[2]
                    sex = i[3]
                    doctor_name = i[4] 
                    fee = i[5]
                    status = "active"
                    i = [patient_id,patient_name,age,sex,doctor_name,fee,status]
                    w.writerow(i)
                    print("Patient's record has been restored")
                else:
                    w.writerow(i)
        else:
            w.writerow(i)
    f.close()
    f1.close()
    os.remove("patient.csv")
    os.rename("temp.csv","patient.csv")
    if found == 0:
        print("Record does not exist")
def searchpatient():
    print("Search a Patient's Record")
    print("==========================")
    f = open("patient.csv","r",newline = "")
    s = input("Enter the Patient's name whose record you want to search:")
    r = csv.reader(f)
    found = 0
    for i in r:
        if i[1]==s:
            found = 1
            if i[6]=="active":
                print("———————————————————————————————————————")
                print("Patient's id :",i[0])
                print("Patient's name :",i[1])
                print("Patient's age :",i[2])
                print("Patient's sex :",i[3])
                print("Name of Doctor :",i[4])
                print("Fee :",i[5])
                print("————————————————————————————————————————")
            else:
                print("Patient record exists")
    f.close()
    if found == 0:
        print("Record does not exist")
def delpatient():
    print("Delete a Patient's Record")
    print("=========================")
    f = open("patient.csv","r",newline = "")
    f1 = open("temp.csv","w",newline = "")
    s = input("Enter the Patient's name whose record you want to delete:")
    r = csv.reader(f)
    w = csv.writer(f1)
    found = 0
    for i in r:
        if i[1]==s:
            found = 1
            if i[6]=="active":
                print("———————————————————————————————————————")
                print("Patient's id :",i[0])
                print("Patient's name :",i[1])
                print("Patient's age :",i[2])
                print("Patient's sex :",i[3])
                print("Name of Doctor :",i[4])
                print("Fee :",i[5])
                print("————————————————————————————————————————")
                choice = input("Do you want to delete this Patient's record?\n(Y/N)").lower()
                if choice=="y":
                    patient_id = i[0]
                    patient_name = i[1]
                    age = i[2]
                    sex = i[3]
                    doctor_name = i[4] 
                    fee = i[5]
                    status = "inactive"
                    i = [patient_id,patient_name,age,sex,doctor_name,fee,status]
                    w.writerow(i)
                    print("Patient record deleted..")
                else:
                    w.writerow(i)
            else:
                print("Patient's record is already deleted")
                w.writerow(i)
        else:
            w.writerow(i)
    if found == 0:
        print("Record does not exist")   
    f.close()
    f1.close()
    os.remove("patient.csv")
    os.rename("temp.csv","patient.csv") 
def listofpatients():
    print("================================================================================")
    print("                               List of all Patients                             ")               
    print("================================================================================")   
    f = open("patient.csv","r",newline = "")
    r = csv.reader(f) 
    for i in r:
        if i[6]=="active":
            print("———————————————————————————————————————")
            print("Patient id :",i[0])
            print("Patient name :",i[1])
            print("Patient age :",i[2])
            print("Patient sex :",i[3])
            print("name of doctor :",i[4])
            print("fee :",i[5])
        else:
            pass
    f.close()   
def menu():
    
    choice = 0
    while choice!=6:
        print("\n")
        print("MENU:--")
        print("===============================================")
        print("1. Add a New Patient Record")
        print("2. Modify an Existing Patient Record")
        print("3. Search a Patient Record")
        print("4. Deleting an Existing Patient Record")
        print("5. List of Patients")
        print("6. Exit")
        print("===============================================")
        choice = input("Enter Your Choice:")
        if choice=="1":
            newpatient()
        elif choice=="2":
            editpatient()
        elif choice=="3":
            searchpatient()
        elif choice=="4":
            delpatient()
        elif choice=="5":
            listofpatients()
        elif choice=="6":
            print("Software Exited.....")
            break
        else:
            if choice.isalpha():
                print("Invalid Character")
            elif choice.isdigit():
                print("invalid choice")
            else:
                print("invalid character")
def login():
    c = 'y'
    login = 0
    print("\n")
    print("————————————————————————————————————————————————————————————————————————————")
    print("————————————————————————————————————————————————————————————————————————————")
    print("||                   ««« Hospital Management System »»»                   ||")
    print("————————————————————————————————————————————————————————————————————————————")
    print("————————————————————————————————————————————————————————————————————————————")
    print("||                 ««« By Kartika Verma and Apoorv Jha »»»                ||")
    print("\n")
    while c == 'y':
        password = input("Enter the password:")
        if password=="hospital1":
            login = 1
            break
        else:
            c = input("Incorrect password\nTry Again?  (y/n)").lower()
    if login == 1:
        menu()        
login()               
    
 

      
