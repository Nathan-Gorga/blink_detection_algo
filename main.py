import matplotlib.pyplot as plt

from printData import extract_eeg_data, printBuffer, segmentChannelData
from buffer import bufferSizesFromChannel


if __name__ == "__main__":
    path = r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    bufferSize = 150
    buffer = bufferSizesFromChannel(channels[0],bufferSize)
    print(buffer)
    printBuffer(channels[0],buffer)
    plt.show()
    


