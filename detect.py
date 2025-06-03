### going to try several methods of detection and see which one is fastest, most reliable and capable of working on the fly

import numpy as np



def cleanDetect(isBlink):
    previous = False
    size = len(isBlink)
    for i in range(size):
        temp = previous
        previous = isBlink[i]
        if isBlink[i] and temp:
            
            isBlink[i] = False
    return isBlink
            
                

def detectWithThreshold(bChannel,threshold=150):
    
    ret = []
    for buffer in bChannel:   
        ret.append(any(buffer[:,1] >= threshold))    
    return cleanDetect(ret)