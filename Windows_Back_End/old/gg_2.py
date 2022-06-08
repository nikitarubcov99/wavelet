# import cv2
# import numpy
# import numpy as np
# # img = cv2.imread("Data\\lena_black_spots_mask.bmp")
#
#
# from PIL import Image
#
# #read the image
# from matplotlib import pyplot as plt
#
# import cv2
# import numpy
# import numpy as np
#
# # read input
# from matplotlib import pyplot as plt
#
# img = cv2.imread("Data\\Image\\test.png")
# # img = cv2.imread("im_gray.png", 1)
#
# #############################################################
# im_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('Grayscale', im_gray)
# print('gg')
#
# cv2.imwrite('im_gray.png', im_gray)
# #############################################################
#
#
#
# # img = cv2.imread("lena_black_spots_mask.png")
#
# # low = (0,0,0)
# # high = (0,0,0)
#
# # mask = cv2.inRange(im_gray, (0,0,0), (127, 127, 90))
# mask = cv2.inRange(img, (0, 0, 0), (127, 127, 127))
# mask = 255 - mask
# print('gg')
#
#
#
#
#
#
#
# # save output
# cv2.imwrite('lena_black_spots_mask.png', mask)
# print('gg')
#
# # numpy.savetxt('ssssd', (coords), fmt="%d")
#
#
#
# #
# # plt.figure(figsize=(17, 5))
# # plt.title("График с изображения")
# # plt.plot(coords)  # строим график - ось `X` - первый столбец, `Y` - второй
# # plt.show()
#
# cv2.imshow('img', img)
# print('gg')
#
# # cv2.imshow('mask', mask)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
# #
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # im = Image.open("lena_black_spots_mask.png")
# im = Image.open("lena_black_spots_mask.png")
#
# #rotate image by 90 degrees
# angle = 270
# out = im.rotate(angle, expand=True)
# out.save('rotate-lena_black_spots_mask.png')
#
# img_1 = cv2.imread('rotate-lena_black_spots_mask.png')
#
# arr = np.asarray(img_1)
# black_pixels = np.array(np.where(arr == 0))
# black_pixel_coordinates = list(zip(black_pixels[0], black_pixels[1]))
#
#
#
#
# # print(black_pixel_coordinates)
#
# # numpy.savetxt('ssssd111', black_pixel_coordinates, fmt="%d")
#
# # print('gg')
#
#
#
# from itertools import groupby
#
# res = [max(g) for _,g in groupby(black_pixel_coordinates, lambda x: x[0])]
# numpy.savetxt('ssssd111', res, fmt="%d")
#
# # print(res)
#
#
# # plt.figure(figsize=(17, 5))
# plt.title("График с изображения")
# plt.plot(res)  # строим график - ось `X` - первый столбец, `Y` - второй
# plt.show()
# print('gg')
import numpy as np
import matplotlib.pyplot as plt
"""
Sukhbinder
5 April 2017
Based on:    
"""

def _rect_inter_inner(x1,x2):
    n1=x1.shape[0]-1
    n2=x2.shape[0]-1
    X1=np.c_[x1[:-1],x1[1:]]
    X2=np.c_[x2[:-1],x2[1:]]
    S1=np.tile(X1.min(axis=1),(n2,1)).T
    S2=np.tile(X2.max(axis=1),(n1,1))
    S3=np.tile(X1.max(axis=1),(n2,1)).T
    S4=np.tile(X2.min(axis=1),(n1,1))
    return S1,S2,S3,S4

def _rectangle_intersection_(x1,y1,x2,y2):
    S1,S2,S3,S4=_rect_inter_inner(x1,x2)
    S5,S6,S7,S8=_rect_inter_inner(y1,y2)

    C1=np.less_equal(S1,S2)
    C2=np.greater_equal(S3,S4)
    C3=np.less_equal(S5,S6)
    C4=np.greater_equal(S7,S8)

    ii,jj=np.nonzero(C1 & C2 & C3 & C4)
    return ii,jj

def intersection(x1,y1,x2,y2):
    """
INTERSECTIONS Intersections of curves.
   Computes the (x,y) locations where two curves intersect.  The curves
   can be broken with NaNs or have vertical segments.
usage:
x,y=intersection(x1,y1,x2,y2)
    Example:
    a, b = 1, 2
    phi = np.linspace(3, 10, 100)
    x1 = a*phi - b*np.sin(phi)
    y1 = a - b*np.cos(phi)
    x2=phi
    y2=np.sin(phi)+2
    x,y=intersection(x1,y1,x2,y2)
    plt.plot(x1,y1,c='r')
    plt.plot(x2,y2,c='g')
    plt.plot(x,y,'*k')
    plt.show()
    """
    ii,jj=_rectangle_intersection_(x1,y1,x2,y2)
    n=len(ii)

    dxy1=np.diff(np.c_[x1,y1],axis=0)
    dxy2=np.diff(np.c_[x2,y2],axis=0)

    T=np.zeros((4,n))
    AA=np.zeros((4,4,n))
    AA[0:2,2,:]=-1
    AA[2:4,3,:]=-1
    AA[0::2,0,:]=dxy1[ii,:].T
    AA[1::2,1,:]=dxy2[jj,:].T

    BB=np.zeros((4,n))
    BB[0,:]=-x1[ii].ravel()
    BB[1,:]=-x2[jj].ravel()
    BB[2,:]=-y1[ii].ravel()
    BB[3,:]=-y2[jj].ravel()

    for i in range(n):
        try:
            T[:,i]=np.linalg.solve(AA[:,:,i],BB[:,i])
        except:
            T[:,i]=np.NaN


    in_range= (T[0,:] >=0) & (T[1,:] >=0) & (T[0,:] <=1) & (T[1,:] <=1)

    xy0=T[2:,in_range]
    xy0=xy0.T
    return xy0[:,0],xy0[:,1]


if __name__ == '__main__':

    # a piece of a prolate cycloid, and am going to find
    a, b = 1, 2
    phi = np.linspace(3, 10, 100)
    x1 = a*phi - b*np.sin(phi)
    y1 = 2*a - b*np.cos(phi)

    x2=phi
    y2=np.sin(phi)+1.5
    x,y=intersection(x1,y1,x2,y2)
    plt.plot(x1,y1,c='r')
    plt.plot(x2,y2,c='g')
    plt.plot(x,y,'*k')
    plt.show()