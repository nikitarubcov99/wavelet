import matplotlib
import numpy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyedflib import highlevel

# read an edf file
signals, signal_headers, header = highlevel.read_edf('Data\\EDF\\1234e.edf')
print(signals)  # prints 256

gg = signal_headers[1]
print(gg)

try:
    dd = gg.get('sample_frequency')
    print(dd)

except KeyError:
    print('Такого ключа нет')


"""
форматы:
[ECG1 [ 0.5     0.4692  0.4504 ...  0.1462  0.0788 -0.0516]
 ECG2 [-0.1518 -0.1658 -0.1808 ... -0.306  -0.4402 -0.5856]
 ECG3 [-0.652  -0.635  -0.6314 ... -0.4524 -0.5192 -0.534 ]
 aVR [-0.174  -0.1516 -0.1346 ...  0.0798  0.1806  0.3186]
 aVL [ 0.576   0.552   0.5408 ...  0.2994  0.299   0.2412]
 aVF [-0.402  -0.4004 -0.406  ... -0.3792 -0.4798 -0.5598]]

"""
global signal
signal = signals[1]


A_ = signal[11250:13500]

# from IPython.display import display
from biosppy.signals import ecg
import biosppy.plotting as pl
# from wfdb import processing
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
# import wfdb
import scipy.signal as ss
from sklearn.cluster import KMeans


# record = wfdb.rdrecord('s0553_re', pb_dir='ptbdb/patient290/',sampto = 50000, channels = [0])
# wfdb.plot_wfdb(record=record)
# display(record.__dict__)

# f = open('data.txt', 'w')
# f.write("# Simple Text Format\n")
# f.write("# Sampling Rate (Hz):= 1000.00\n")
# f.write("# Resolution:= 12\n")
# f.write("# Labels:= ECG\n")
# for x in record.p_signal:
#     f.write(str(x[0]) + "\n")
# f.close()
# xxx = open("data.txt")
# s=xxx.readlines()[4:]
#
#
#
# signal0 = np.loadtxt("data.txt")


sampling_rate = 1000.0
order = int(0.3 * sampling_rate)
filtered, _, _ = ecg.st.filter_signal(signal=A_, ftype='FIR', band='bandpass', order=order, frequency=[3, 45], sampling_rate= 1000.)
rpeaks = ecg.hamilton_segmenter(signal = filtered, sampling_rate=1000.)
rpeaks = list(rpeaks)
arr = []
for i in rpeaks[0]:
    arr.append(i)
print("Обычные пики:", arr)





before = 200
after = 400
R = np.sort(rpeaks)
print(rpeaks)

length = len(A_)
templates = []
print(templates)

for j in R:
    for i in j:
        a = i - before
        print(a)

        # if a < 0:
        #     continue
        b = i + after
        print(b)

        # if b > length:
        #     break
        templates.append(A_[a:b])
        print(templates)

templates = np.array(templates)




print("участки", templates)





templates_ = list(templates)
templates__ = []
for i in templates_[0]:
    templates__.append(i)
print("участки", templates__)





# print("участки", templates)


#
# rpeaks, = ecg.correct_rpeaks(signal=filtered,rpeaks=arr, sampling_rate=sampling_rate, tol=0.05)
# #print("Модифицированные пики:", list(rpeaks))
# #print("Отфильтрованный сигнал:", list(filtered))
# filtered = filtered.tolist()
# len_x = 50000
# mass = []
# file = open('temp.txt','w')
# for r in rpeaks:
#     if r+400 > len_x - 1:
#         rpeaks = rpeaks[:-1]
#         break
#     for i in range(-200,400,1):
#         mass.append(filtered[r+i])
#         file.write(str(filtered[r+i]) + "\n")
#     #print(len(mass))
# file.close()
# x = range(0,len_x)
# plt.plot(x, filtered)
# plt.show(True)
# plt.clf()
# '''for i in list(range(1,len(rpeaks))):
# 	plt.plot(list(range(0,600)),mass[i*600:i*600 + 600])
# plt.show(True)'''
#
# '''rs_mean = []
# tt = []
# for k in range(0,600):
#     ar_means = []
#     for idx in range(0,int(len(mass)/600)):
#         ar_means.append(mass[idx*600 + k])
#     mean = (np.mean(ar_means).tolist())
#     rs_mean.append(mean)'''
#
# res_mean = []
# for k in range(0,600):
#     arr_means = []
#     for idx in range(0,int(len(mass)/600)):
#         arr_means.append(mass[idx*600 + k])
#     X = np.array(arr_means).reshape(len(arr_means), 1)
#     mean = (np.mean(KMeans(n_clusters = 5).fit(X).cluster_centers_)).tolist()
#     res_mean.append(mean)
# '''plt.plot(list(range(0,600)), res_mean)
# plt.show(True)'''
#
# N = 10
# result2 = np.convolve(res_mean, np.ones((N,))/N, mode='same')
# '''plt.plot(list(range(0,600)), result2, list(range(0,600)), rs_mean)
# plt.show(True)'''