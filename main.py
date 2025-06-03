import matplotlib.pyplot as plt


from printData import extract_eeg_data, printBuffer, printOneChannel, segmentChannelData, printThreshold, printBlinks
from buffer import bufferSizesFromChannel, bufferChannel
from detect import detectWithThreshold

if __name__ == "__main__":
    
    path = r'C:\Users\n.gorga\code\processRawData\data\raise_eyebrows_one_second_while_blink_nathan.xdf'
    raw_data = extract_eeg_data(path)
    channels = segmentChannelData(raw_data)
    bufferSize = 10
    buffer = bufferSizesFromChannel(channels[0],bufferSize)
    
    bChannel = bufferChannel(channels[0],buffer)
    threshold = 150 #TODO : automatically calibrate the threshold
    isBlink = detectWithThreshold(bChannel,threshold)

 

    # printThreshold(channels[0],threshold,buffer)
    
    
    printBlinks(channels[0],bufferSize,isBlink)
    
    plt.show()