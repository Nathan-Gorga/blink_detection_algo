import numpy as np
from printData import extract_eeg_data
from buffer import segmentChannelData,bufferChannel,bufferSizesFromChannel
from detect import cleanDetect
import matplotlib.pyplot as plt

def findAverageBlinkHeight(isBlink, bChannel):
    total = 0
    num = 0
    
    for blink,channel in zip(isBlink,bChannel):
        if blink:
            total += max(channel)
            num += 1
    
    return total / num


#this calibration is intentionnaly crude for now, we are going to impove it as flase positives and false negatives come in
def calibrate(path=r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sample_blinks_nathan.xdf'):

    raw_data = extract_eeg_data(path)
    
    raw_channels = segmentChannelData(raw_data)
    
    
    channels = []
    for raw_channel in raw_channels:
        channels.append(raw_channel[:,1])
        
    
    bufferSize = 10
    buffer = bufferSizesFromChannel(channels[0],bufferSize)
    
    bChannel = bufferChannel(channels[0],buffer)
    
    # find maximal point
    
    maxPoint = max(channels[0])
    
    # find baseline
    
    baseline = np.mean(channels[0]) # when measuring calibration, make sure a lot of the sample does not contain the signal, mostly noise
    
    # use 60% for threshold
    
    threshold = (maxPoint - baseline) * 0.6
       
    # use this for detecing blinks
    
    isBlink = messyDetectWithThreshold(bChannel,threshold)
    
    #find the average blink height
    
    avgBlinkHeight = findAverageBlinkHeight(isBlink,bChannel)
    
    
    
    #return 75% of that average
    return avgBlinkHeight * 0.75

def messyDetectWithThreshold(bChannel,threshold=150):
    
    ret = []
    for buffer in bChannel:   
        ret.append(any(buffer[:] >= threshold))    
    return cleanDetect(ret)