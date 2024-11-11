# Used on the Host Machine to Receive Tactile Data from RPi

import socket
import numpy as np

import numpy as np
import matplotlib.pyplot as plt
import os


HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 65432

NUM_VALUES = 50
NUM_SENSORS = 12

# Function for connecting to the RPi via TCP
def receive_data():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('ready')
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(NUM_SENSORS * NUM_VALUES * 8)  # Assuming each value is 2 bytes (16-bit)
            received_array = np.frombuffer(data, dtype=np.float64).reshape((NUM_SENSORS, NUM_VALUES))
    return received_array


# Parameters
sampling_rate = 20  # Hz    

data = receive_data()


# Create a figure
fig, ax = plt.subplots()

cax = ax.imshow(data, cmap='hot', interpolation='nearest', vmin=0, vmax=3.3)


# Set ticks
ax.set_xticks(range(NUM_VALUES))
ax.set_yticks(range(NUM_SENSORS))

# Directory to save the plots


ax.set_axis_off()

# CHANGE to be the directory you want
save_dir = 'C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\data\\test_images'


os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# Save the plot with a label in the filename
label = 0  # Example label
# filename = input("image name: ")
filename = f'test.jpg'
file_path = os.path.join(save_dir, filename)
plt.savefig(file_path, bbox_inches='tight', pad_inches=0, transparent=False)  # Save the plot as an image file
plt.close(fig)  # Close the figure to free up memory
plt.show()












# import socket
# import numpy as np

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.colors import Normalize, ListedColormap
# import os


# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 65432

# NUM_VALUES = 50
# NUM_SENSORS = 12
# MAX_VALUE = 3.3
# THRESHOLD_VOLTAGE = 3.3

# def receive_data():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print('ready')
#         conn, addr = s.accept()
#         with conn:
#             print('Connected by', addr)
#             data = conn.recv(NUM_SENSORS * NUM_VALUES * 8)  # Assuming each value is 2 bytes (16-bit)
#             received_array = np.frombuffer(data, dtype=np.float64).reshape((NUM_SENSORS, NUM_VALUES))
#             # print(received_array)
#     return received_array


# data = receive_data()

# normalized_data = data / MAX_VALUE


# # # # Create a figure
# # # fig, ax = plt.subplots()
# # dpi = 96
# # fig, ax = plt.subplots(figsize=(NUM_VALUES/dpi, NUM_SENSORS/dpi), dpi=dpi)

# # Define threshold value

# threshold = THRESHOLD_VOLTAGE / MAX_VALUE

# # Create a custom colormap
# cmap = plt.get_cmap('hot')
# newcolors = cmap(np.linspace(0, 1, 256))
# newcolors[int(threshold * 255):, :] = np.array([1, 1, 0, 1])  # Set colors over the threshold to yellow
# newcmap = ListedColormap(newcolors)


# # Create an image plot
# # cax = ax.imshow(data, cmap='hot', interpolation='bicubic')
# # cax = ax.imshow(data, cmap=newcmap, interpolation='bicubic', norm=Normalize(vmin=0, vmax=threshold))

# # fig.colorbar(cax)

# # Set labels
# # ax.set_xlabel('Time Steps')
# # ax.set_ylabel('Sensors')
# # ax.set_title('Sensor Readings Over Time')

# # Set ticks
# # ax.set_xticks(np.arange(NUM_VALUES))
# # ax.set_yticks(np.arange(NUM_SENSORS))

# # Directory to save the plots


# # ax.set_axis_off()
# save_dir = 'C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\data\\binary_dataset\\train\\good'
# # save_dir = 'C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\binary_dataset\\train\\bad'
# # save_dir = 'C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\binary_dataset\\test\\good'
# # save_dir = 'C:\\Users\\cbgno\\OneDrive\\Desktop\\SURP\\test_nn\\binary_dataset\\test\\bad'

# os.makedirs(save_dir, exist_ok=True)  # Create directory if it doesn't exist

# norm = Normalize(vmin=0, vmax=1)
# normalized_data = norm(data)
# image = newcmap(normalized_data)

# filename = input("image name: ")
# file_path = os.path.join(save_dir, filename)
# plt.imsave(file_path, image)
# # plt.savefig(file_path, dpi=dpi, bbox_inches='tight', pad_inches=0, transparent=True)  # Save the plot as an image file
# plt.show()
# # plt.close(fig)  # Close the figure to free up memory

