import matplotlib.pyplot as plt

from printData import extract_eeg_data, printBuffer, printOneChannel, segmentChannelData, printThreshold
from buffer import bufferSizesFromChannel, bufferChannel
from detect import detectWithThreshold

if __name__ == "__main__":
    path = r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    bufferSize = 150
    buffer = bufferSizesFromChannel(channels[0],bufferSize)
    print(buffer)
    bChannel = bufferChannel(channels[0],buffer)
    threshold = 150
    test = detectWithThreshold(bChannel,threshold)
    print(test)
 

    printThreshold(channels[0],threshold,buffer)
    
    plt.show()