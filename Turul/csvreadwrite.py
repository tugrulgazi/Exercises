# -*- coding: utf-8 -*-
 import csv

with open("onemliolaylar.csv",'r', newline='') as f:
    readcsv = csv.reader(f, delimiter='.')
    for row in readcsv:
        print(",".join(row))
#******************************************************************************        
with open("employee_birthday.csv",'r',newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =",")
    linecount=0
    for row in csv_reader:
        if linecount==0:
            print("Column names are : " + ", ".join(row))
            linecount += 1
        else:
            print('{} works in the {} department and was born in {}'.format(row[0],row[1],row[2]))
#******************************************************************************            
newemployees = [['Eric','IT','December'],['Monica','IT','July']]


with open("employee_birthday.csv",'a',newline='') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerows(newemployees)
#******************************************************************************
while True:
    
    name = str(input("Enter the name of new employee: "))
    department = str(input("Enter the department of new employee: "))
    birthmonth = str(input("Enter the birthmonth of new employee: "))
    newemp = [name,department,birthmonth]
    
    with open("employee_birthday.csv",'a',newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(newemp)
    print("\n{} is succesfully added.".format(name))
    
    decision = input("Do you want to add a new employee?\n(Y,N)\n")
    
    if (decision == 'N' or decision == 'n'):
        break
    else:
        continue

print("Have a nice day!")
        


    

    
    