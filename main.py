from eegDataProcessor import XDFDataUI
import pyxdf
import numpy as np

import matplotlib.pyplot as plt



"""
the data is formatted like this :"""


def extract_eeg_data(xdf_path):
    streams, _ = pyxdf.load_xdf(xdf_path)
    
    
    for stream in streams:
        data = np.array(stream['time_series'])
        return data

    raise RuntimeError("Aucun flux EEG trouvé dans le fichier .xdf.")


def printOneChannel(channel_data, color, num):
    # X-axis: sample indices (time)
    x = np.arange(len(channel_data))
    
    # Y-axis: channel values (e.g., position)
    y = channel_data[:, 1]  # or 0 depending on which value you want plotted

    plt.scatter(x, y, color=color, label=f'Channel {num}', s=10)

    # Draw connecting lines between consecutive points (left to right)
    plt.plot(x, y, color=color, linewidth=0.5)

    plt.xlabel("Sample Index")
    plt.ylabel("Channel Value")
    plt.title("Channel Signal Progression")
    plt.legend()
    plt.grid(True)
    plt.show()


    
 


if __name__ == "__main__":
    path = r'C:\Users\n.gorga\code\processRawData\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
  
    printOneChannel(np.array(raw_data),"red",1)

    # for data in raw_data:
    #     print(data)

