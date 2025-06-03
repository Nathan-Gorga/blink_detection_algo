import pyxdf
import numpy as np

import matplotlib.pyplot as plt




def printChannels(channels, colors=None):
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
    





def printOneChannel(channel_data, color='blue', num=1, name=None):
    """
    Plots a single EEG channel's 2D data (x and y values) over sample indices.

    Parameters:
    - channel_data: Nx2 array with x and y data for one channel.
    - color: matplotlib color for the plot.
    - num: channel number (for labeling).
    """
    # X-axis: time/sample index
    time = np.arange(len(channel_data))
    
    # Y-axis: vertical signal value (e.g., position, voltage, etc.)
    y = channel_data  # using only y-dimension for signal shape

    plt.figure(figsize=(10, 4))
    
    plt.plot(time, y, color=color, linewidth=0.8, label=name)
    plt.scatter(time, y, color=color, s=5)

    plt.xlabel("Sample Index")
    plt.ylabel("Signal Value")
    plt.title(name)
    plt.grid(True)
    plt.legend()





def printBuffer(channel_data, buffers):
    printOneChannel(channel_data, "blue") 
    
    for buffer_point in buffers:
        plt.axvline(x=buffer_point, color='green', linestyle='--', linewidth=1)
    
    


def printThreshold(channel_data, threshold,buffer):
    printBuffer(channel_data,buffer)
    plt.axhline(y=threshold, color="orange", linestyle='--', linewidth=1)


def printBlinks(channel_data, step, isBlink):
    printOneChannel(channel_data, "blue") 
    current = 0
    for blink in isBlink:
        if(blink):
            plt.axvline(x=current, color='red', linestyle='--', linewidth=1)
        current += step

    