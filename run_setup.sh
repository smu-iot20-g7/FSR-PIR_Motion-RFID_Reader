#!/bin/bash
cd /Tray_out/SPI-Py/MFRC522-python
sudo python RFID_FSR.py

cd /Tray_in/
sudo python3 Trolley_tray_in.py


