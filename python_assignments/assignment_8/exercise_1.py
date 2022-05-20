# # import sqlite3

# # con = sqlite3.connect('http://knesset.gov.il/Odata/ParliamentInfo.svc/')

# # cur = con.cursor()

# # # Create table
# # cur.execute('''CREATE TABLE stocks
# #                (date text, trans text, symbol text, qty real, price real)''')

# # # Insert a row of data
# # cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# # # Save (commit) the changes
# # con.commit()

# # # We can also close the connection if we are done with it.
# # # Just be sure any changes have been committed or they will be lost.
# # con.close()

import requests
import pyodata


SERVICE_URL = 'http://knesset.gov.il/Odata/Votes.svc/'

client = pyodata.Client(SERVICE_URL, requests.Session())


# count is 44535
# count = client.entity_sets.KNS_Bill.get_entities().count().execute()

# KNS_Bills = client.entity_sets.KNS_Bill.get_entities().select('BillID,KnessetNum').execute()
# KNS_Bills = client.entity_sets.KNS_Bill.get_entities().count().execute()
KNS_Bills = client.entity_sets.vote_rslts_kmmbr_shadow.get_entities().execute()
# KNS_Bills = client.entity_sets.KNS_Bill.get_entity(1).execute()
# KNS_Bills = client.entity_sets.KNS_Committee.get_entities().filter('KnessetNum eq 20').execute()


print(KNS_Bills)
# for KNS_Bill in KNS_Bills:
#     print(KNS_Bill)



# import requests
# import pyodata

# SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

# # Create instance of OData client
# northwind = pyodata.Client(SERVICE_URL, requests.Session())

# employee1 = northwind.entity_sets.Employees.get_entities().execute()
# print(employee1)