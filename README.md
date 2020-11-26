# Force Sensitvity Sensor, PIR Motion Sensor, RFID Reader

Monitor the tray return rates at Beo Crescent Hawker Centre by tracking the number of trays leaving a particular hawker stall and the number of trays return by a cleaner to the trolley. 

## Device Environemnt
All the codes run with python2.7 or python3.7
Raspberry Pi – _sender: To capture the tray in/out counts and send it to a queue system (MQTT)

## Instructions

1) Clone this entire repository to a raspeberryPi 3
2) Run the requirement.txt file
3) Run the bash script - run_setup.sh
4) Ensure Trolley_tray_in.py and RFID_FSR.py is running on the Raspberry Pi.


