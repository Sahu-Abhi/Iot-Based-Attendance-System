from datetime import datetime as dt
first_period = dt.now().hour == 10 and dt.now().minute < 50
second_period = dt.now().hour == 10 and dt.now().minute > 50 or dt.now().hour == 11 and dt.now().minute < 40
third_period = dt.now().hour == 11 and dt.now().minute > 40 or dt.now().hour == 12 and dt.now().minute < 30
fourth_period = dt.now().hour == 12 and dt.now().minute > 30 or dt.now().hour == 13 and dt.now().minute < 20
fifth_period = dt.now().hour == 14 and dt.now().minute > 10 or dt.now().hour == 16 and dt.now().minute < 30
test = dt.now().hour == 19 and dt.now().minute > 00 or dt.now().hour == 24 and dt.now().minute < 30
time_table = {
    0:
        {
            first_period: "DAA",
            second_period: "TOC",
            third_period: "IOT",
            fourth_period: "COA",
            fifth_period: "DAA LAB",
            test: "DAA"
        },
    1:
        {
            first_period: "IOT",
            second_period: "COA",
            third_period: "TOC",
            fourth_period: "DAA",
            fifth_period: "DAA LAB",
        },
    2:
        {
            first_period: "COA",
            second_period: "TOC",
            third_period: "DAA",
            fourth_period: "IOT",
            fifth_period: "IOT LAB",
        },
    3:
        {
            first_period: "DAA",
            second_period: "COA",
            third_period: "IOT",
            fourth_period: "TOC",
            fifth_period: "MINI PROJECT",
        },
    4:
        {
            first_period: "COA",
            second_period: "IOT",
            third_period: "TOC",
            fourth_period: "DAA",
        },
    6: {
            test: "COA"
    }
}
mail = {
    "COA": "test.mail.dev.abhi@gmail.com",
    "DAA": "test.mail.dev.abhi@gmail.com",
    "IOT": "test.mail.dev.abhi@gmail.com",
    "TOC": "test.mail.dev.abhi@gmail.com",
    "DAA LAB": "test.mail.dev.abhi@gmail.com",
    "IOT LAB": "test.mail.dev.abhi@gmail.com",
    "MINI PROJECT": "test.mail.dev.abhi@gmail.com"
}