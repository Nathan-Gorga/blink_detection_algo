# python import libs
import numpy as np
import matplotlib.pyplot as plt


def printOneChannel(channel_data :list[float], color :str = "blue", name :str = ""):

    # use time sample for x coordinates
    x :list[int] = np.arange(len(channel_data))
    
    # signal data in y axis
    y :list[float] = channel_data

    plt.figure(figsize=(10, 4))
    
    plt.plot(x, y, color=color, linewidth=0.8, label=name)

    plt.scatter(x, y, color=color, s=5)
    
    plt.title(name)

    plt.grid(True)

    plt.legend()



def printBufferedChannel(channel_data :list[float], buffer_sizes_for_channel :list[int], color :str = "blue"):
    
    printOneChannel(channel_data, color) 
    
    # overlay the above signal with the buffers
    for buffer_point in buffer_sizes_for_channel:
        
        plt.axvline(x=buffer_point, color='green', linestyle='--', linewidth=1)
    
    

def printSignalWithThreshold(channel_data :list[float], threshold :float , buffer_sizes_for_channel :list[int],color :str = "blue"):

    printBufferedChannel(channel_data,buffer_sizes_for_channel,color)

    #overlay the signal with threshold line
    plt.axhline(y=threshold, color="orange", linestyle='--', linewidth=1)


def printBlinks(channel_data :list[float], buffer_size :int, is_there_blink_in_buffer :list[bool], color :str = "blue"):

    printOneChannel(channel_data, color)
     
    current :int = 0
    
    for blink in is_there_blink_in_buffer:

        if(blink):

            plt.axvline(x=current, color='red', linestyle='--', linewidth=1)

        current += buffer_size

    