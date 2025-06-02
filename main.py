from eegDataProcessor import XDFDataUI
import pyxdf
import numpy as np


def extract_eeg_data(xdf_path):
    streams, _ = pyxdf.load_xdf(xdf_path)
    
    
    for stream in streams:
        data = np.array(stream['time_series'])
        return data

    raise RuntimeError("Aucun flux EEG trouvé dans le fichier .xdf.")



if __name__ == "__main__":
    path = r'C:\Users\n.gorga\code\processRawData\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
    for data in raw_data:
        print(data)

