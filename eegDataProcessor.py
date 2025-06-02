"""
Author : Apoorva Busunur Mallikarjuna
Project : Vigilens
Lab : Centre of Neuroergonomics and Human Factors, DCAS, ISAE SUPAERO
Description : A script to preprocessor EEG data collected using OpenBCI Gangalion system on FP1 and FP2 positions.
Date : 26-05-2025
"""

import numpy as np
import pyxdf
import mne
import matplotlib.pyplot as plt


###turning this into a function to call it in the main code

def XDFDataUI(path=r'C:\Users\n.gorga\code\processRawData\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'):
    # Load XDF file
    xdf_path = path
    streams, file_header = pyxdf.load_xdf(xdf_path)

    # Find EEG stream (by type or name)
    eeg_stream = None
    for stream in streams:
        #print(stream)
        #print(stream['info']['name'][0])

        if stream['info']['type'][0].lower() == 'eeg' or 'eeg' in stream['info']['name'][0].lower():
            eeg_stream = stream
            break

    if eeg_stream is None:
        raise RuntimeError("No EEG stream found in XDF file.")
    

    # Simulated from your provided data
    data = np.array(eeg_stream['time_series']).T  # shape: (n_channels, n_samples)
    sfreq = 200.0  # or use effective_srate if you want: 199.95337694925965

    # Example channel names (customize as needed)
    ch_names = ['EEG 1', 'EEG 2', 'EEG 3', 'EEG 4']
    ch_types = ['eeg'] * len(ch_names)

    # Create MNE info structure
    info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)

    # Create Raw object
    raw = mne.io.RawArray(data, info)

    # Plot or save as needed

    #raw.plot()
    raw.info['bads'] = ['EEG 2', 'EEG 3']
    raw_filtered = raw.copy().filter(l_freq=1.0, h_freq=40.0)
    raw_filtered.plot(scalings=dict(eeg=200),
        duration=5.0,         # seconds per screen
        n_channels=2,         # only show 2 (since you dropped bad ones)
        highpass=1.0,         # high-pass visual filter
        lowpass=40.0          # low-pass visual filter
        )
    #raw_filtered.plot_sensors(ch_type='eeg', show_names=True)  "RuntimeError: No valid channel positions found"

    plt.show()
    # raw.save('your_data_raw.fif', overwrite=True)