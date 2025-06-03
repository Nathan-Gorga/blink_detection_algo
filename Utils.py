import numpy as np
import pyxdf

from Buffer import separateChannelData

def extractEEGData(xdf_path :str):
    streams , _ = pyxdf.load_xdf(xdf_path)
    
    for stream in streams:
        
        data = np.array(stream['time_series'])
        
        return data

    raise RuntimeError("Aucun flux EEG trouvé dans le fichier .xdf.")

def getDataFromFile(path :str):
    
    raw_data :list[list[float]] = extractEEGData(path)
    
    raw_channels :list[list[float]] = separateChannelData(raw_data)
    
    channels :list[list[float]] = []
    
    for raw_channel in raw_channels:
        channels.append(raw_channel[:,1])
        
    return channels