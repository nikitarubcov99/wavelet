# import cv2
# import pywt
import numpy as np
# import scipy
# from matplotlib.pyplot import spy
from numpy import std, conj, subtract, var, polyfit, log10

# import pandas as pd
# import xlrd
# import math

import pywt
# from matplotlib import pyplot as plt
from pyedflib import highlevel

from scipy.fft import fft

signals, signal_headers, header = highlevel.read_edf('Data\\EDF\\1234e.edf')
# signals, signal_headers, header = highlevel.read_edf('Data\\123e.edf')
print(signals) # prints 256
# print(signal_headers[0]['sample_frequency']) # prints 256

A = signals[1]







# db1 = pywt.Wavelet('db1')
# cA3, cD3, cD2, cD1 = pywt.wavedec(x, db1)
# print(cA3)
# print(cD3)
# print(cD2)
# print(cD1)

"""Длинна сигнала"""
A_length = len(A)
print(A_length)
A_ = A[11250:13500]
A__length = len(A_)
print(A__length)


# filename = 'Norm.xlsx'
# A = pd.read_excel(filename)
# A.head()
db1 = pywt.Wavelet('db4')
Fr = 0.7143
# Исправить частоты, рассчитанные по формуле
Fr1 = 367.15
Fr2 = 183.57
Fr3 = 91.79
# (cA2, cD2), (cA1, cD1) = pywt.swt(A, db1,  level=2)


cD3, cD2, cD1 = pywt.wavedec(A_, db1, level=2)
cA4 = pywt.wavedec(A_, db1, level=2)

DDDcD1 = pywt.upcoef('d', cD1, wavelet= db1, level=2)
DDDcD2 = pywt.upcoef('d', cD2, wavelet= db1, level=2)
DDDcD3 = pywt.upcoef('d', cD3, wavelet= db1, level=2)

print('################################################################################')

print('"""Статическое среднее"""')

Sd1 = std(cD1)
Sd2 = std(cD2)
Sd3 = std(cD3)
ScD1 = std(DDDcD1)
ScD2 = std(DDDcD2)
ScD3 = std(DDDcD3)
print(f'Вейвлет-коэффициент cD1: {Sd1}')
print(f'Вейвлет-коэффициент cD2: {Sd2}')
print(f'Вейвлет-коэффициент cD3: {Sd3}')
print(f'Компонент сигнала ScD1: {ScD1}')
print(f'Компонент сигнала ScD2: {ScD2}')
print(f'Компонент сигнала ScD3: {ScD3}')
print('################################################################################')

print('"""Энтропия Шенона"""')

data = pywt.wavedec(A_, db1)
S = 0
Etot = 0
for d in data:
    E = d**2
    P = E/np.sum(E)
    S = -np.sum(P*np.log(P))
    Etot = np.sum(E)
    print(f"Энтропия Шенона: {S}")
    # print(f"Энергия: {Etot}")
    # E1 = Etot / S  # отношение энергии вейвлета к энтропии Шеннона
    #
    # print(f"Отношение энергии вейвлета к энтропии Шеннона: {E1}")
print('################################################################################')

print('"""Енергитический спектр"""')

Len_s_1 = len(DDDcD1)
YS1 = fft(DDDcD1)
PS1 = YS1*conj(YS1)/Len_s_1

Len_s_2 = len(DDDcD2)
YS2 = fft(DDDcD2)
PS2 = YS2*conj(YS2)/Len_s_2

Len_s_3 = len(DDDcD3)
YS3 = fft(DDDcD3)
PS3 = YS3*conj(YS3)/Len_s_3
print('################################################################################')




print('"""Покатели Херста"""')



#
# import numpy as np
#
# """Compute the Hurst exponent of sig.
#
#
# arguments
#     sig -- 1D signal
# returns
#     hurst_exponent -- float
# """
# sig = pywt.wavedec(A_, db1)
# n = sig.size # num timesteps
# t = np.arange(1, n + 1)
# y = sig.cumsum() # marginally more efficient than: np.cumsum(sig)
# mean_t = y / t # running mean
#
# s_t = np.zeros(n)
# r_t = np.zeros(n)
#
# for i in range(n):
#     s_t[i] = np.std(sig[:i + 1])
#     x_t = y - t * mean_t[i]
#     r_t[i] = np.ptp(x_t[:i + 1])
#
# r_s = r_t / s_t
# r_s = np.log(r_s)[1:]
# n = np.log(t)[1:]
# a = np.column_stack((n, np.ones(n.size)))
# [hurst_exponent, c] = np.linalg.lstsq(a, r_s)[0]
# print(f'длводыолв{hurst_exponent}')
#




"""Неприрывный вейвлет-анализ кардиосигнала"""

# f = pywt.swt(A_, db1)
# исправить!!!!!
# plt.figure(figsize=(17, 5))
# plt.title("Энергетический спектр PS3")
# plt.plot(A_)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title("Энергетический спектр PS3")
# plt.plot(f)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#





# from pywt import dwt2, idwt2
# img = cv2.imread('Data\\111.jpg')
# cA, (cD) = dwt2(img, 'db4')
#
# Mc = np.size(img, 0)
# Nc = np.size(img, 1)
# dd = idwt2((cA,(cD)),'db4')[:Mc,:Nc]
#
# print(dd)





# plt.figure(figsize=(17, 5))
# plt.title("Энергетический спектр PS3")
# plt.plot(dd)
# plt.show()


# print(cA2)
# print(cA1)
# print(cA3)
# print(cD3)
# print(cD2)
# print(cD1)
# print(DDDcD1)
# print(DDDcD2)
# print(DDDcD3)

# plt.plot(DDDcD1)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.xlim([5000, 5500])
# plt.ylim([0, -1])

#_____________________________________________________Вывод Графиков____________________________________________________


# plt.figure(figsize=(17, 5))
# plt.title("Входной сигнал")
# # plt.plot(A)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.plot(A_)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title("Разложение сигнала до уровня 1")
# plt.plot(cD1)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title("Разложение сигнала до уровня 2")
# plt.plot(cD2)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title("Разложение сигнала до уровня 3")
# plt.plot(cD3)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title(f"Компоненты сигнала на частоте {Fr1} Hz")
# plt.plot(DDDcD1)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title(f"Компоненты сигнала на частоте {Fr2} Hz")
# plt.plot(DDDcD2)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title(f"Компоненты сигнала на частоте {Fr3} Hz")
# plt.plot(DDDcD3)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
# plt.figure(figsize=(17, 5))
# plt.title("Энергетический спектр PS1")
# plt.plot(PS1)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title("Энергетический спектр PS2")
# plt.plot(PS2)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
#
# plt.figure(figsize=(17, 5))
# plt.title("Энергетический спектр PS3")
# plt.plot(PS3)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
########################################################################################################################
#
# [c,l]=wavedec(A,3,w)
# cA3=appcoef(c,l,w,3)
# [cD1,cD2,cD3]=detcoef(c,l,[1,2,3])
# figure (1)
# >> plot(A); title('ECG norm')




# plt.subplot(1, 2, 1)
# plt.imshow(mask, cmap="gray")
# plt.subplot(1, 2, 2)
# plt.imshow(result)
# plt.show()