import matplotlib.pyplot as plt
import numpy as np

from printData import extract_eeg_data, printBuffer, printOneChannel, printThreshold, printBlinks
from buffer import bufferSizesFromChannel, bufferChannel, segmentChannelData
from detect import detectWithThreshold
from calibration import calibrate

from calibration import findAverageBlinkHeight

if __name__ == "__main__":
    
    path = r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sample_blinks_nathan.xdf'

    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    bufferSize = 10
    buffer = bufferSizesFromChannel(channels[0],bufferSize)
    
    bChannel = bufferChannel(channels[0],buffer)
    
    
    
    baseline = np.mean(channels[0][:,1])
    
    

    threshold = calibrate(r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sample_blinks_nathan.xdf')



    isBlink = detectWithThreshold(bChannel,threshold)

 

    # printThreshold(channels[0],threshold,buffer)
    
    
    printBlinks(channels[0],bufferSize,isBlink)
    
    plt.axhline(y=baseline, color="grey", linestyle='--', linewidth=1)
    plt.axhline(y=threshold, color="orange", linestyle='--', linewidth=1)
    
    plt.show()