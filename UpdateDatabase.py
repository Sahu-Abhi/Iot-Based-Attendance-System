import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyC1iDJajiW-SkqWG4q7SNLfesWdqnGVLZg",
    "authDomain": "iot-attendance-db.firebaseapp.com",
    "projectId": "iot-attendance-db",
    "databaseURL": "https://iot-attendance-db-default-rtdb.firebaseio.com/",
    "storageBucket": "iot-attendance-db.appspot.com",
    "messagingSenderId": "957461254262",
    "appId": "1:957461254262:web:863547c4f02da08f41cf57",
    "measurementId": "G-XH3Y3PQ4J4",
}


class UpdateDb:

    def __init__(self):
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        self.database = self.firebase.database()

    def update_data(self, data, date, subject):
        self.database.child(f"{subject}").child(f"{date}").set(data)





# ------------------------------------------------------------------------------
# Create Data

# database.push(data)
# database.child("Students").child("DAA").set(data)

# ------------------------------------------------------------------------------
# Read Data

# read_data = database.child("Students").child("DAA").get()
# print(read_data.val())

# ------------------------------------------------------------------------------
# Update Data

# database.child("Students").child("DAA").update({})