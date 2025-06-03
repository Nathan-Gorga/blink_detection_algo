### going to try several methods of detection and see which one is fastest, most reliable and capable of working on the fly

import numpy as np

def detectWithThreshold(bChannel,threshold=150):
    
    ret = []
    for buffer in bChannel:   
        ret.append(any(buffer[:,1] >= threshold))    
    return ret