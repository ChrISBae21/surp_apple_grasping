# Used on the RPi to Sample sensors and send data to the Host Machine

import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

import time
import numpy as np
import socket

ads0 = ADS.ADS1115(i2c, address=0x48)
ads1 = ADS.ADS1115(i2c, address=0x49)
ads2 = ADS.ADS1115(i2c, address=0x4A)
ads3 = ADS.ADS1115(i2c, address=0x4B)

channels = [
    [AnalogIn(ads0, ADS.P0), AnalogIn(ads0, ADS.P1), AnalogIn(ads0, ADS.P2)],
    [AnalogIn(ads1, ADS.P0), AnalogIn(ads1, ADS.P1), AnalogIn(ads1, ADS.P2)],
    [AnalogIn(ads2, ADS.P0), AnalogIn(ads2, ADS.P1), AnalogIn(ads2, ADS.P2)],
    [AnalogIn(ads3, ADS.P0), AnalogIn(ads3, ADS.P1), AnalogIn(ads3, ADS.P3)]
]


# Set up the socket for communication with the host PC
HOST = '10.0.0.205' # Replace with actual IP of HOST PC
PORT = 65432 # Port to listen on (should be > 1023)

def send_data_to_host(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data.tobytes()) # Send the data as bytes
        
# Parameters
sampling_rate = 20 # Hz
num_readings = 50 # Number of readings (time steps)
num_sensors = 12 # Number of sensors

# Initialize Data Array
data = np.zeros((num_sensors, num_readings))

print('initialized')

# Data collection
for i in range(num_readings):
    start_time = time.time()
    for ads_index, ads_channels in enumerate(channels):
        for ch_index, ch in enumerate(ads_channels): # Calculate the global index for 3 channels per ADS1115
            if ch.voltage <= 0.000:
                data[ads_index * 3 + ch_index, i] = 0
            else:
                data[ads_index * 3 + ch_index, i] = ch.voltage # Read the sensor value
                
            
        
    time.sleep(max(0, (1.0 / sampling_rate) - (time.time() - start_time)))
    
# Send data to host PC
print('done')
print(data)
send_data_to_host(data)
    

