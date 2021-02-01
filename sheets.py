import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from datetime import datetime as dt
from gspread_dataframe import get_as_dataframe, set_with_dataframe




def GetDf():
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials
    import pandas as pd
    from datetime import datetime as dt
    from gspread_dataframe import get_as_dataframe, set_with_dataframe
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("CREDS.json" , scope)
    client = gspread.authorize(creds)
    sheet = client.open("weight_test").sheet1
    dtframe = get_as_dataframe(sheet, usecols=[0, 1, 2, 3, 4, 5, 6, 7])
    dtframe['DATE'] = pd.to_datetime(dtframe['DATE']).dt.date
def DataF():
    return dtframe.dropna(thresh=1)

#crown_test = client.open("crown_test")
#project spreadsheet

# project_test_sheet = crown_test.get_worksheet(0)
# ptframe = get_as_dataframe(project_test_sheet, usecols=[0,1,2,3,4,5,6,7])
# pt = ptframe.dropna(thresh=1)
# #client spreadsheet
# client_test_sheet = crown_test.get_worksheet(1)
# ctframe = get_as_dataframe(client_test_sheet, usecols=[0,1,2,3,4,5,6])
# ct = ctframe.dropna(thresh=1)
# #po spreadsheet
# po_test_sheet = crown_test.get_worksheet(2)
# poframe = get_as_dataframe(po_test_sheet, usecols= [0,1,2,3,4,5])
# po = poframe.dropna(thresh=1)
# #invoice spreadsheet
# invoice_test_sheet  = crown_test.get_worksheet(3)
# invframe = get_as_dataframe(invoice_test_sheet, usecols=[0,1,2,3,4,5,6])
# inv = invframe.dropna(thresh=1)


