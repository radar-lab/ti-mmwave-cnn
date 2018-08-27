import rospy
import rosbag
import numpy as np
import math
# import matplotlib.pyplot as plt
# from micro_doppler_pkg.msg import MicroDoppler
# from ti_mmwave_rospkg.msg import RadarScan

bag = rosbag.Bag('./rosbag/2018-06-13-17-21-34.bag')
for msg in bag.read_messages(topics=['/ti_mmwave/micro_doppler']):
    msg_handle = msg.message
    time_domain_bins = msg_handle.time_domain_bins
    nd = msg_handle.num_chirps
    break
x = np.empty((0,time_domain_bins*nd), float)
# print(self.x.shape)
for msg in bag.read_messages(topics=['/ti_mmwave/micro_doppler']):
    msg_handle = msg.message
    mds_array = np.array(msg_handle.micro_doppler_array).reshape((nd, time_domain_bins))
    mds_array[int(nd/2),] = 0
    temp = mds_array.reshape((1,-1))
    print(temp.shape)
    print(max(temp[0,:]))
    if max(temp[0,:]) != 0:
        mds_array_norm = temp / max(temp[0,:])
    else:
        mds_array_norm = temp
    x = np.append(x, mds_array_norm, axis = 0)
print(x.shape)
np.savetxt('./output/test.csv', x, delimiter=",")