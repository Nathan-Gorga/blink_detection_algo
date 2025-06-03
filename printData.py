import pyxdf
import numpy as np

import matplotlib.pyplot as plt


def extract_eeg_data(xdf_path):
    streams, _ = pyxdf.load_xdf(xdf_path)
    
    
    for stream in streams:
        data = np.array(stream['time_series'])
        return data

    raise RuntimeError("Aucun flux EEG trouvé dans le fichier .xdf.")

def printAllChannels(channels, colors=None):
    num_channels = len(channels)
    if num_channels == 0:
        print("No channels to display.")
        return

    if colors is None:
        colors = ['red', 'blue', 'green', 'orange']

    # Handle up to 4 subplots in 1 column
    fig, axs = plt.subplots(num_channels, 1, figsize=(12, 3 * num_channels), sharex=True)

    if num_channels == 1:
        axs = [axs]  # make it iterable

    for i, (channel_data, ax) in enumerate(zip(channels, axs)):
        x = np.arange(len(channel_data))
        y = channel_data[:, 1]  # Assuming column 1 is denoised signal

        ax.scatter(x, y, color=colors[i % len(colors)], s=10, label=f'Channel {i+1}')
        ax.plot(x, y, color=colors[i % len(colors)], linewidth=0.5)
        ax.set_ylabel("Y")
        ax.set_title(f"Channel {i+1}")
        ax.legend()
        ax.grid(True)
        ax.axis('equal')

    axs[-1].set_xlabel("Sample Index")
    fig.suptitle("EEG Channels", fontsize=14)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()



def segmentChannelData(raw_data):
    numChannels = raw_data.shape[1] // 2
    channels = []

    for i in range(numChannels):
        x = raw_data[:, 2 * i]
        y = raw_data[:, 2 * i + 1]
        channel_data = np.stack((x, y), axis=1) 
        channels.append(channel_data)

    return channels
