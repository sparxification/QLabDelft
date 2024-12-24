#!/usr/bin/env python
# coding: utf-8


# Installeer de bibliotheek pyserial eenmalig, zet er daarna een hekje/hash-teken voor.
#!pip install pyserial
import serial
import matplotlib.pyplot as plt
#%matplotlib qt
import numpy as np
import time
import serial.tools.list_ports
from IPython.display import display, clear_output
#from matplotlib.ticker import MaxNLocator


print("Make sure you have the Arduino uploaded with the right .ino")
print("Data serial output must be in the form of seconds+1decimal;data for example: 40.5;12456")
print("Make sure the Arduino is connected, and the serial port is not in use.")
print("")

# Search for the USB port
ports = list(serial.tools.list_ports.comports())
if not ports:
    print("no USB-device found...")
    print("possible connection or driver problem")
    print("")
    port = "NOT FOUND"
else:
    for p in ports: #find all serial device ports in use (usually one)
        port = p.device
        print("The Arduino is probably connected to "+ port)

print("(press Enter for defaults:)")

# Serial port settings
serial_port_str = input("Enter the serial port, if different than "+ port+ " :" )
# Use the default value if the user presses Enter without typing anything
serial_port = serial_port_str if serial_port_str else port

# Ask the user for the communication speed of the Arduino (baudrate)
#baud_rate_str = input("Enter the baud_rate, default 9600: ")
#baud_rate = int(baud_rate_str) if baud_rate_str else 9600
baud_rate = 9600

# Ask the user for the max number of data points
#max_data_points_str = input("Enter the max. number of data points, default 100000: ")
#max_data_points = int(max_data_points_str) if max_data_points_str else 100000
max_data_points = 100000

# Ask the user for the number of seconds to record
max_time_str = input("Enter the record duration in seconds, default 25: ")
max_time = int(max_time_str) if max_time_str else 29 # we lose 4 seconds somehow, and start at 0.

#print("(whatever comes first)")

# Lists to record data
values1 = [] # the timestamps
values2 = [] # the values from sensor


# Create a serial connection
ser = serial.Serial()
ser.baudrate=baud_rate
ser.port=serial_port
while True:
    try:
        ser.close()
        time.sleep(1)
        ser.open()
        print("Serial opened")
        time.sleep(1)
        read=ser.readline() # test the first line of data, this data we throw away...
        #print(read.decode('utf-8'))
        print("Busy collecting data...")
        break  # Exit this loop if start is successful
    except:
        print("Failed to start or read serial. Retrying in 1 second...")
        time.sleep(1)  # Wait for 1 second before retrying

        
# Set up the plot
plt.figure()
plt.ion()  # Interactive mode on

# Infinite loop to read data from the serial port and plot it
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()  # Read a line of data and decode it
        
        try:
            # Split the line by semicolon
            data = line.split(';')
            
            # Parse the values
            value1 = float(data[0])  # First value (e.g., 40.5) timestamp
            value2 = int(data[1])    # Second value (e.g., 0) value from sensor

            # Append the values to lists
            values1.append(value1)
            values2.append(value2)

            # Clear the previous output to avoid plotting over the old data
            clear_output(wait=True)
            plt.clf
            
            # Plot the updated data
            plt.plot(range(len(values1)), values2, '.', markersize=10, c='blue') # plot, but cheat a bit on the time axis....looks a bit nicer.
            #plt.plot(values1, values2, '.', markersize=10, c='blue') # plot without cheating. 
            plt.title('De lichtsterkte als functie van de tijd')
            plt.xlabel('tijd [s]')
            plt.ylabel('lichtsterkte [ongecalibreerd]')
            # Gebruik MaxNLocator om de minimale stapgrootte van de y-ticks op 5 te zetten
            #ax = plt.gca()  # Krijg de huidige as
            #ax.yaxis.set_major_locator(MaxNLocator(integer=True, steps=[5, 200]))
            if np.max(values2) < 100 : # Set vertical step size to a reasonable value when measuring only noise or light pollution, data is zoomed out.
                plt.ylim(0,100)
            else   : 
                plt.ylim(np.min(values2)*0.96, np.max(values2)*1.01) # Set vertical scaling so data is not too far zoomed in.
            plt.xlim(0,max_time+1)  # Set horizontal scaling to the record time set at start. 
            
            plt.grid()
            
            # Show the plot
            #display(plt.gcf())  # Display the updated figure
            
            plt.pause(0.1)  # Pause to allow the plot to refresh
                                   
            if values1[-1]-values1[0] > max_time or len(values2) >= max_data_points:
                print("Data acquisition has ended, please restart & clear kernel for next try only if necessary.")
                print("You can save your plot image by right-clicking.")
                ser.close()
                break
        
        except (ValueError, IndexError):
            # Handle any parsing errors
            print("Invalid data received:", line)



