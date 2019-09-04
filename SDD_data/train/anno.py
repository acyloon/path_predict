# coding:UTF-8
# $B<jF0$G%G!<%?$rA*JL$9$k%W%m%0%i%`(B
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob

DATA = './deathCircle/*/'
IMAGE= './deathCircle/*/'
SAVE_DATA = 'annotations10.txt'
SAVE_IMAGE= 'image.png'

def main():
    # $BFI$_9~$`%G%#%l%/%H%j;XDj(B
    data_path, image_path = os.path.join(DATA), os.path.join(IMAGE)
    data_path, image_path = glob(data_path), glob(image_path)
    data_path.sort()
    image_path.sort()
    # $B%G%#%l%/%H%jKh$K%G!<%?$H2hA|$rFI$_9~$`(B
    for p, i in zip(data_path, image_path):
        data = np.genfromtxt(p + 'annotations2.txt', delimiter=' ')
        unique_id = np.unique(data[:, 0])
        image = cv2.imread(i + 'reference.jpg')
        print((image.shape))
        # $B3JG<$9$kG[Ns$rMQ0U(B
        save_array = np.empty((0, 10), dtype=np.int32)
        # $B%G!<%?%;%C%H$N(BID$BKh$KFI$_9~$`(B
        for id in unique_id:
            data_id = data[data[:, 0] == id, :]
            # $BCj=P$7$?(BID$B$+$i8+$($J$$BP>]$O:o=|$7!"(B(x,y)$B:BI8$rCj=P(B
            data_id = data_id[data_id[:, 6] == 0, :]
            x = (data_id[:, 1] + data_id[:, 3])/2
            y = (data_id[:, 2] + data_id[:, 4])/2
            plt.figure()
            plt.imshow(image)
            plt.xlim(0, image.shape[1])
            plt.ylim(image.shape[0], 0)
            plt.plot(x, y, color='b', linewidth='1')
            plt.savefig(i + SAVE_IMAGE)
            plt.clf()
            plot_image = glob(i + SAVE_IMAGE)
            plot_image = cv2.imread(plot_image[0])
            # $B%-!<%\!<%I%$%Y%s%H(B
            while True:
                cv2.imshow(str(id), plot_image)
                key = cv2.waitKey(1)&0xff
                # q$B$,2!$5$l$?$i2?$b$7$J$$(B
                if key == ord('q'):
                    os.remove(i + SAVE_IMAGE)
                    cv2.destroyAllWindows()
                    break
                # s$B$,2!$5$l$?$iG[Ns$K3JG<(B
                elif key == ord('s'):
                    save_array = np.append(save_array, data_id, axis=0)
                    # $B2hA|$N:o=|(B
                    os.remove(i + SAVE_IMAGE)
                    cv2.destroyAllWindows()
                    break
        # $B%F%-%9%H$rJ]B8(B
        np.savetxt(p + SAVE_DATA, save_array, fmt='%.1d', delimiter=' ')

if __name__ == '__main__':
    main()