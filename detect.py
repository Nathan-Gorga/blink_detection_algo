

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
        ret.append(any(buffer[:] >= threshold))    
    return cleanDetect(ret)