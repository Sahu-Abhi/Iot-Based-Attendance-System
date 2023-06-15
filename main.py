import requests
import smtplib
from time_table import time_table, mail
from datetime import datetime
from datetime import time as t, datetime as dt
import pandas as pd
from email.message import EmailMessage
from UpdateDatabase import UpdateDb
from GSheet import GSHEET


EMAIL = "test.mail.dev.abhi@gmail.com"
PASSWORD = "omyfflrpblbjfazc"

today_date = dt.now().date()
week_day = dt.now().weekday()
# print(today_date)


curr_hour = datetime.now().time().hour
curr_min = datetime.now().time().minute
curr_time = t(curr_hour, curr_min, 0, 0)
mail_timings = [t(10, 30, 0, 0), t(11, 20, 0, 0), t(12, 10, 0, 0), t(13, 0, 0, 0), t(14, 40, 0, 0), t(11, 41, 0, 0)]
# print(curr_time)

if curr_time in mail_timings:
    current_subject = time_table[week_day][True]
    email_id = mail[current_subject]
    print(email_id)

    sheet_id = "1iYcgKxSc06rEm9u836cIYGzc2fnxL02VobB4OH6lVXQ"
    df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
    data = df.to_dict()
    df.to_excel("data.xlsx")
    print(data)

    # TODO : Send data to respective subject teacher

    msg = EmailMessage()
    msg['Subject'] = f"{today_date} Attendance Sheet"
    msg['From'] = EMAIL
    msg['To'] = email_id
    msg.set_content('Test Mail')

    with open('data.xlsx', 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='vnd.ms-excel', filename=f"{today_date}-{current_subject}.xlsx" )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
        connection.login(user=EMAIL, password=PASSWORD)
        connection.send_message(msg)

     # TODO : Update the data to permanent record
    database = UpdateDb()
    SHEET_ENDPOINT = "https://api.sheety.co/c9019aeda39054ccde8a20b71458a5c8/ioTAttendanceSystem/sheet1"

    response = requests.get(url=SHEET_ENDPOINT)
    data_db = response.json()["sheet1"]

    database.update_data(data_db, today_date, current_subject)
    # TODO : Clear the data from IoT attendance sheet
    gsheet = GSHEET()
    gsheet.clear_record()



# time formatting of sheet time
# hour = int(data['sheet1'][0]['time'].split(":")[0])
# minute = int(data['sheet1'][0]['time'].split(":")[1])
# time = t(hour, minute, 0, 0)
# print(time)





