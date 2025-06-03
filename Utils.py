import numpy as np
import pyxdf

from Buffer import *

def extract_eeg_data(xdf_path):
    streams, _ = pyxdf.load_xdf(xdf_path)
    
    
    for stream in streams:
        data = np.array(stream['time_series'])
        return data

    raise RuntimeError("Aucun flux EEG trouvé dans le fichier .xdf.")

def getDataFromFile(path):
    
    raw_data = extract_eeg_data(path)
    
    raw_channels = segmentChannelData(raw_data)
    
    channels = []
    
    for raw_channel in raw_channels:
        channels.append(raw_channel[:,1])
        
    return channels