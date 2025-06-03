def bufferSizesFromChannel(channel_data,bufferSize=150):

    channelSize = len(channel_data)
    
    bufferStartPoints = [0]
    check = bufferSize
    while check <= channelSize:
        bufferStartPoints.append(check)
        check += bufferSize
        
    return bufferStartPoints
    