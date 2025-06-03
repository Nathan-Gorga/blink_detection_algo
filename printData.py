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

def printTwoBlinks(channel1, channel2, buffer_size, is_there_blink_in_buffer1,is_there_blink_in_buffer2, name,color1="blue",color2="red"):
    axis1 = plt.subplot(2,1,1)
    plt.title(name)

    plt.grid(True)

    
    axis2 = plt.subplot(2,1,2)

    plt.grid(True)

    plt.legend()

    x :list[int] = np.arange( np.max( len(channel1))) 
    
    # signal data in y axis
    y1 :list[float] = channel1
    y2 :list[float] = channel2

    
    
    axis1.plot(x, y1, color=color1, linewidth=0.8, label="Channel 1")
    axis2.plot(x, y2, color=color2, linewidth=0.8, label="Channel 2")

    axis1.scatter(x, y1, color=color1, s=5)
    axis2.scatter(x, y2, color=color2, s=5)
    
    current :int = 0
    
    for blink1,blink2 in zip(is_there_blink_in_buffer1,is_there_blink_in_buffer2):

        if(blink1):

            axis1.axvline(x=current, color='green', linestyle='--', linewidth=1)

        if(blink2):

            axis2.axvline(x=current, color='green', linestyle='--', linewidth=1)

        current += buffer_size
    
    
    
    return [axis1,axis2]
    
    