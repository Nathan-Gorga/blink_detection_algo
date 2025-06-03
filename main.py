from eegDataProcessor import XDFDataUI
import pyxdf
import numpy as np

import matplotlib.pyplot as plt


def extract_eeg_data(xdf_path):
    streams, _ = pyxdf.load_xdf(xdf_path)
    
    
    for stream in streams:
        data = np.array(stream['time_series'])
        return data

    raise RuntimeError("Aucun flux EEG trouvé dans le fichier .xdf.")

def printOneChannel(channel_data, color='blue', num=1):
    # X-axis: sample indices (time)
    x = np.arange(len(channel_data))
    
    # Y-axis: channel values (position)
    # I think channel_data[:, 0] might be the noise separated from the data, comming from the D_G electrode, therefore we can ignore it
    y = channel_data[:, 1]  

   

    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, color=color, label=f'Channel {num}', s=10)

    # Draw lines between consecutive points in the same array 
    plt.plot(x, y, color=color, linewidth=0.5)

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Raw 2D Data - Channel {num} with Connecting Lines")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')


def segmentChannelData(raw_data):
    numChannels = raw_data.shape[1] // 2
    channels = []

    for i in range(numChannels):
        x = raw_data[:, 2 * i]
        y = raw_data[:, 2 * i + 1]
        channel_data = np.stack((x, y), axis=1) 
        channels.append(channel_data)

    return channels


if __name__ == "__main__":
    path = r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    printOneChannel(channels[0],"red",1)
    
    plt.show()
    


