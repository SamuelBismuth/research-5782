import sqlite3
import requests
import xmltodict
import os


URL = "http://knesset.gov.il/Odata/ParliamentInfo.svc/KNS_BillInitiator()/"

response = requests.get(URL)

kns_bill_initiatior = xmltodict.parse(response.content)

table_name = kns_bill_initiatior['feed']['title']['#text']

properties = list(kns_bill_initiatior['feed']['entry'][1]['content']['m:properties'].keys())


if not os.path.exists('kns_bill_initiatior.db'):
    con = sqlite3.connect('kns_bill_initiatior.db')
    cur = con.cursor()

    try:
        # print('CREATE TABLE {0} ({1})'.format(table_name, str(properties)[1:-1]).replace('d:', ''))
        cur.execute('CREATE TABLE {0} ({1})'.format(table_name, str(properties)[1:-1]).replace('d:', ''))
    except sqlite3.OperationalError as error:
        print(error)

    for entry in kns_bill_initiatior['feed']['entry']:
        # print('INSERT INTO {0} VALUES ({1})'.format(table_name, str([entry['content']['m:properties'][property]['#text'] for property in properties])[1:-1]))
        cur.execute('INSERT INTO {0} VALUES ({1})'.format(table_name, str([entry['content']['m:properties'][property]['#text'] for property in properties])[1:-1]))

    con.commit()
    con.close  # We have to close the connector to create the file.

con = sqlite3.connect('kns_bill_initiatior.db')
cur = con.cursor()

for row in cur.execute('SELECT * FROM {0}'.format(table_name)):
    print(row)

con.close()

