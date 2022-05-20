from oauth2client.service_account import ServiceAccountCredentials
import gspread

from parse import parse_c_A_b
from steinitz import steinitz_ip

scopes = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name("my-key.json", scopes) 
file = gspread.authorize(credentials) 

sheet = file.open("Research Algorithm")  

try: 
    input = sheet.worksheet("Input")
except AttributeError:
    input = sheet.add_worksheet(title="Input", rows=10000, cols=200)

try: 
    output = sheet.worksheet("Output")
except AttributeError:
    output = sheet.add_worksheet(title="Output", rows=100, cols=20)

# Read the input sheet.
c, A, b = parse_c_A_b(input.get_all_values())

# Write in the output sheet.
output.update_acell('A1', steinitz_ip(c, A, b))