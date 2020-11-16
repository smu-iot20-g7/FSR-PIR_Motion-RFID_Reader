import time
from datetime import datetime
from pymongo import MongoClient


db = MongoClient("mongodb+srv://root:0NqePorN2WDm7xYc@cluster0.fvp4p.mongodb.net/iot?retryWrites=true&w=majority")

# Welcome message
print("RFID Detected!")
print("FSR Detected")

fsr_status = 1
rfid_status = 1
process_status = True
current_time = datetime.now()
print("Time is: " + str(current_time))
print("Weight sensor: " + str(fsr_status))

print("RFID and Weight Dected")

if process_status and fsr_status == 1:
    print("RFID and Weight Dected")
    posts = db.fsr_rfid.collection
    post_data = {
        'timestamp': current_time,
        'rfid_status': rfid_status,
        'fsr_status': fsr_status
    }

    result = posts.insert_one(post_data)
    print("Inserted with ID: " + str(result))


