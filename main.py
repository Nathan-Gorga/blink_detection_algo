# python lib imports
import matplotlib.pyplot as plt
from Calibration import calibrate

# my lib imports
from Calibration import calibrate
from Utils import getDataFromFile
from Buffer import segmentChannelByBuffer
from Detect import detectWithThreshold
from PrintData import printTwoBlinks

def detectBlinksFromChannels(channel_data1 :list[float], channel_data2 :list[float], threshold1 :float,threshold2 :float, name):

    buffer_size = 10
    
    segmented_channel_by_buffer1 :list[list[float]] = segmentChannelByBuffer(channel_data1, buffer_size)
    segmented_channel_by_buffer2 :list[list[float]] = segmentChannelByBuffer(channel_data2, buffer_size)
    
    is_there_blink_in_buffer1 :list[bool] = detectWithThreshold(segmented_channel_by_buffer1, threshold1)
    is_there_blink_in_buffer2 :list[bool] = detectWithThreshold(segmented_channel_by_buffer2, threshold2)
    
    [axis1,axis2] = printTwoBlinks(channel_data1,channel_data2, buffer_size, is_there_blink_in_buffer1, is_there_blink_in_buffer2,name)

    axis1.axhline(y=threshold1, color="orange", linestyle='--', linewidth=1)
    axis2.axhline(y=threshold2, color="orange", linestyle='--', linewidth=1)
    
    plt.show()




if __name__ == "__main__":
    
    path :str = r'data\three_fast_blinks_nathan.xdf'
    
    # calibration 
    [threshold1, threshold2, baseline1, baseline2]  = calibrate(path) 
    
    # path of .xdf file

    channels :list[list[float]] = getDataFromFile(path)# handle the second channel and detect on it too
    
    channels[0] -= baseline1
    channels[1] -= baseline2
    
    detectBlinksFromChannels(channels[0],channels[1],threshold1,threshold2,path)

    