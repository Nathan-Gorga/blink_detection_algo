# import python libs
import numpy as np

def bufferSizesFromChannel(channel_data :list[float], bufferSize :int = 150):

    channel_size : int = len(channel_data)
    
    buffer_start_points :list[int] = [0]

    check :int = bufferSize

    while check <= channel_size:

        buffer_start_points.append(check)

        check += bufferSize
        
    return buffer_start_points
    
    
def bufferChannel(channel_data :list[float], buffer_sizes_for_channel :list[int]):
    
    buffer_list_size = len(buffer_sizes_for_channel)

    buffered_channel :list[float] = []

    for i in  range(buffer_list_size - 1): #-1 to prevent overflow with i+1

        start = buffer_sizes_for_channel[i]

        stop = buffer_sizes_for_channel[i+1]

        buffered_channel.append(channel_data[start:stop])
        
    return buffered_channel


def separateChannelData(raw_data :list[list[float]]):

    num_channels :int = raw_data.shape[1] // 2
    channels :list[list[float]] = []

    for i in range(num_channels):

        x = raw_data[:, 2 * i] 

        y = raw_data[:, 2 * i + 1]

        channel_data = np.stack((x, y), axis=1) 

        channels.append(channel_data)

    return channels