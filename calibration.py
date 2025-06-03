# python lib imports
import numpy as np

# my lib imports
from Detect import detectWithThreshold
from Buffer import segmentChannelByBuffer
from Utils import getDataFromFile

def findAverageBlinkHeight(is_there_blink_in_buffer :list[bool], segmented_channel_by_buffer :list[list[float]]):

    total = num = 0
    
    for blink, channel in zip(is_there_blink_in_buffer, segmented_channel_by_buffer):

        if blink:

            total += np.max(channel)

            num += 1


    try:
        
        return total / num 

    except ZeroDivisionError:

        return 0


#this calibration is intentionnaly crude for now, we are going to impove it as flase positives and false negatives come in
def calibrate(path=r'data\calibration\calibration_data_nathan.xdf'):

    calibration_channel :list[float] = getDataFromFile(path)[0] # TODO : make a better calibration data set, later will be done before blink detection
        
    buffer_size :int = 10
    
    # find maximal point
    
    max_point :float = np.max(calibration_channel)
    print(max_point)
    
    # find baseline
    
        # when measuring calibration, make sure a lot of the sample does not contain the signal, mostly noise
        # we might just let 15 seconds pass and allow the subject to blink normally to calibrate on this data
    
    baseline :float = np.mean(calibration_channel) 

    # use 65% for threshold
    
    percent_decrease :float = 0.65
        
    first_threshold :float = (max_point - baseline) * percent_decrease
       
    # use this for detecting blinks

    segmented_channel_by_buffer :list[list[float]] = segmentChannelByBuffer(calibration_channel, buffer_size)
    
    is_there_blink_in_buffer :list[bool] = detectWithThreshold(segmented_channel_by_buffer,first_threshold)
    
    #find the average blink height
    
    avg_blink_height :float = findAverageBlinkHeight(is_there_blink_in_buffer,segmented_channel_by_buffer)
    
    if avg_blink_height == 0 : return baseline
    
    return avg_blink_height * percent_decrease # threshold used for rest of algo

