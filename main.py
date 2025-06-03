# python lib imports
import matplotlib.pyplot as plt
import numpy as np

# my lib imports
from PrintData import *
from Buffer import *
from Detect import *
from Calibration import *
from Utils import *


if __name__ == "__main__":
    # calibration 
    threshold :float = calibrate() 
    
    # path of .xdf file
    path :str = r'data\three_fast_blinks_nathan.xdf'

    channels :list[list[float]] = getDataFromFile(path)
    
    
    bufferSize :int = 10
    
    buffer_sizes_for_channel :list[int] = bufferSizesFromChannel(channels[0],bufferSize)
    
    segmentedChannelByBuffer :list[list[float]] = bufferChannel(channels[0],buffer_sizes_for_channel)
    
    isThereBlinkInBuffer :list[bool] = detectWithThreshold(segmentedChannelByBuffer,threshold)
    
    printBlinks(channels[0],bufferSize,isThereBlinkInBuffer)
    
    plt.axhline(y=threshold, color="orange", linestyle='--', linewidth=1)
    
    plt.show()