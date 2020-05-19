import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/igor-bond/Desktop/test sheets-80913ea7370d.json", scope)

client = gspread.authorize(creds)

sheet = client.open("sheet_api_tutorial").sheet1

data = sheet.get_all_records()

row = sheet.row_values(3)
col = sheet.col_values(3)
cell = sheet.cell(3,3).value

NewRaw = [4,'D','John']
#sheet.insert_row(row,4)
#sheet.delete_row(4)
#sheet.update_row(5,NewRow)
sheet.update_cell(2,2,"Changed")
sheet.insert_row(NewRaw,5)


#pprint(cell)