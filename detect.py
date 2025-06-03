# import python libs
import numpy as np

# to remove duplicate detections of the same blink
def cleanDetect(is_there_blink_in_buffer :list[bool]):

    previous :bool = False

    size :int = len(is_there_blink_in_buffer)

    for i in range(size):

        temp :bool = previous

        previous :bool = is_there_blink_in_buffer[i]

        if is_there_blink_in_buffer[i] and temp:
            
            is_there_blink_in_buffer[i] = False

    return is_there_blink_in_buffer
            
                
def detectWithThreshold(segmented_channel_by_buffer :list[list[float]], threshold :int = 150):
    
    ret :list[bool] = []

    for buffer in segmented_channel_by_buffer:   

        ret.append(any(buffer[:] >= threshold))    

    return cleanDetect(ret)