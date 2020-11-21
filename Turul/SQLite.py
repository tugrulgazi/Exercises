# -*- coding: utf-8 -*-
import sqlite3

connection = sqlite3.connect("chinook.db")

# cursor = connection.execute("""select FirstName,LastName 
#                             from customers 
#                             where Fax like '+%' 
#                             order by FirstName,LastName desc""")

# for row in cursor:
#     print("FirstName : "+ row[0])
#     print("LastName : "+ row[1])
#     print("--------------------")

# connection.close()

# -----------------------------------------------------------------------------

# cursor = connection.execute(""" select city,count(*) 
#                             from customers 
#                             group by City
#                             having count(*)>1
#                             order by city """)

# cursor2 = connection.execute(""" select city,count(*) 
#                             from customers 
#                             group by City
#                             having count(*)=1
#                             order by city """)
# for row in cursor:
#     print("City : "+ row[0])
#     print("Count : "+ str(row[1]))
#     print("*"*(len(row[0])+7))
# for row2 in cursor2:
#     print("City : "+ row2[0])
#     print("Count : "+ str(row2[1]))
#     print("*"*(len(row2[0])+7))

#------------------------------------------------------------------------------    










































    

