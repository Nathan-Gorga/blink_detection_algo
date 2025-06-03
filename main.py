import matplotlib.pyplot as plt

from printData import extract_eeg_data, printBuffer, printOneChannel, segmentChannelData
from buffer import bufferSizesFromChannel, bufferChannel


if __name__ == "__main__":
    path = r'C:\Users\gorga\CodeProjects\Arduino\Blink\blink_detection_algo\data\sub-P001_ses-S001_task-Default_run-001_eeg.xdf'
    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    bufferSize = 150
    buffer = bufferSizesFromChannel(channels[0],bufferSize)
    print(buffer)
    bChannel = bufferChannel(channels[0],buffer)
    printOneChannel(bChannel[2],name="buffer 1")
    printOneChannel(bChannel[4],name="buffer 2")
    printBuffer(channels[0],buffer)
    
    
    # printBuffer(channels[0],buffer)
    plt.show()
    


