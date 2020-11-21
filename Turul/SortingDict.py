# -*- coding: utf-8 -*-
students = {"Josh":90,"Brittany":100,"Tim":80,"Tammy":80,'Tom':80}
import pandas as pd
df = pd.DataFrame({"Student":["Lily","Lu","Josh","Brittany","Tom","Tim","Tam"],
                  "Grades":[20,20,90,100,80,80,80]})
print("Unsorted DataFrame\n"+str(df)+"\n")
df = df.sort_values(by=['Grades','Student'],ascending=(False,True))
print("Sorted DataFrame\n"+str(df)+"\n")

for indeks,a in df.iterrows():
     print(str(a["Student"])+ " : " +str(a["Grades"]))
    

# print(dict(sorted(students.items())))
# print(sorted(students))

# # for i in sorted(students):
# #     print(i,":",str(students[i]))
# a = dict(sorted(students.items(), key=lambda x:x[1],reverse = True))
# print(a)
# for key,value in a.items():
#     print("{} : {}".format(key,value))
# for i in range(len(a)):
#     for key,value in a.items():
#         if value[i]==value[i+1]:
#             if key[i]<key[i+1]:
                

# "students = [['Josh',90],["Brittany",100],['Tim',80],['Tam',80],['Tom',80],['Ac',30],['Ab',30]]

# sorted_byvalues = sorted(students,key = lambda x:x[1],reverse = True)
# # print(sorted_byvalues)
# for a in range(len(sorted_byvalues)-1):
#     for i in range(len(sorted_byvalues)-1-a):
#         if sorted_byvalues[i][1] == sorted_byvalues[i+1][1]:
#             if sorted_byvalues[i][0]> sorted_byvalues[i+1][0]:
#                 sorted_byvalues[i],sorted_byvalues[i+1] =sorted_byvalues[i+1],sorted_byvalues[i]
# print(sorted_byvalues)






# for (key,value) in a:
#     a = len(key)
#     print(key," "*(10-a),":",value)

# grades = []
# for value in students.values():
#     grades.append(value)
# grades = sorted(grades,reverse=True)
# print(grades)


    

