# import modules
import gspread
from gspread import Cell, Spreadsheet
import pandas

cred_file = "credentials.json"
gc = gspread.service_account(cred_file)
scope = ["https://www.googleapis.com/auth/spreadsheets"]


class GSHEET:

    def __init__(self):
        # Establish the connection
        self.database = gc.open("IoT Attendance Records")

        # selecting a worksheet
        self.wks = self.database.worksheet("Sheet1")

        # list all available worksheet
        self.li_wks = self.database.worksheets()

    def clear_record(self):
        self.wks.clear()




# add worksheet
# database.add_worksheet("new_sheet", "100", "20")

# Access all the records
# wks.clear()
# df = pandas.DataFrame(wks.get_all_records())
# print(df)







