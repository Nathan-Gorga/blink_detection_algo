def bufferSizesFromChannel(channel_data,bufferSize=150):

    channelSize = len(channel_data)
    
    bufferStartPoints = [0]
    check = bufferSize
    while check <= channelSize:
        bufferStartPoints.append(check)
        check += bufferSize
        
    return bufferStartPoints
    
    
def bufferChannel(channel_data, bufferStarts):
    
    bufferListSize = len(bufferStarts)
    bufferedChannel = []
    for i in  range(bufferListSize - 1): #-1 to prevent overflow with i+1
        start = bufferStarts[i]
        stop = bufferStarts[i+1]
        bufferedChannel.append(channel_data[start:stop])
        
    return bufferedChannel