# python lib imports
import matplotlib.pyplot as plt
from Calibration import calibrate

# my lib imports
from Calibration import calibrate
from Utils import getDataFromFile
from Buffer import segmentChannelByBuffer
from Detect import detectWithThreshold
from PrintData import printBlinks


if __name__ == "__main__":
    # calibration 
    threshold :float = calibrate() 
    
    # path of .xdf file
    path :str = r'data\three_fast_blinks_nathan.xdf'

    channels :list[list[float]] = getDataFromFile(path)
    
    buffer_size = 10
    
    segmented_channel_by_buffer = segmentChannelByBuffer(channels[0], buffer_size)
    
    is_there_blink_in_buffer :list[bool] = detectWithThreshold(segmented_channel_by_buffer,threshold)
    
    printBlinks(channels[0],buffer_size,is_there_blink_in_buffer)
    
    plt.axhline(y=threshold, color="orange", linestyle='--', linewidth=1)
    
    plt.show()