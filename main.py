
from printData import extract_eeg_data,segmentChannelData,printAllChannels

if __name__ == "__main__":
    path = r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    numChannels = len(channels[0])
    # Plot up to 4 channels in separate subplots
    printAllChannels(channels[:numChannels])



