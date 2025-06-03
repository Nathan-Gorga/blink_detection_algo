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

    calibration_channels :list[float] = getDataFromFile(path) # TODO : make a better calibration data set, later will be done before blink detection

    calibration_channel1 = calibration_channels[0]
    calibration_channel2 = calibration_channels[1]
    
    # find baseline
    
        # when measuring calibration, make sure a lot of the sample does not contain the signal, mostly noise
        # we might just let 15 seconds pass and allow the subject to blink normally to calibrate on this data
    
    baseline1 :float = np.mean(calibration_channel1) 
    baseline2 :float = np.mean(calibration_channel2) 

    # put both channels baseline at 0
    calibration_channel1 -= baseline1
    calibration_channel2 -= baseline2
        
    buffer_size :int = 10
    
    # find maximal point
    
    max_point1 :float = np.max(calibration_channel1)
    max_point2 :float = np.max(calibration_channel2)

    # use 65% for threshold
    
    percent_decrease :float = 0.65
        
    first_threshold1 :float = max_point1 * percent_decrease
    first_threshold2 :float = max_point2 * percent_decrease    
       
    # use this for detecting blinks

    segmented_channel_by_buffer1 :list[list[float]] = segmentChannelByBuffer(calibration_channel1, buffer_size)
    segmented_channel_by_buffer2 :list[list[float]] = segmentChannelByBuffer(calibration_channel2, buffer_size)
    
    is_there_blink_in_buffer1 :list[bool] = detectWithThreshold(segmented_channel_by_buffer1,first_threshold1)
    is_there_blink_in_buffer2 :list[bool] = detectWithThreshold(segmented_channel_by_buffer2,first_threshold2)
    
    
    #find the average blink height
    
    avg_blink_height1 :float = findAverageBlinkHeight(is_there_blink_in_buffer1,segmented_channel_by_buffer1)
    avg_blink_height2 :float = findAverageBlinkHeight(is_there_blink_in_buffer2,segmented_channel_by_buffer2)
    
    
    if avg_blink_height1 == 0 or avg_blink_height2 == 0 : raise(ZeroDivisionError)
    
    return [avg_blink_height1 * percent_decrease, avg_blink_height2 * percent_decrease, baseline1, baseline2] # threshold  and baselines used for rest of algo

