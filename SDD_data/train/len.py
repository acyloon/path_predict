# coding:UTF-8
# $B<jF0$G%G!<%?$rA*JL$9$k%W%m%0%i%`(B
import os
import numpy as np
from glob import glob

DATA = './*/*/'

def main():
    # $BFI$_9~$`%G%#%l%/%H%j;XDj(B
    data_path = os.path.join(DATA)
    data_path = glob(data_path)
    data_path.sort()
    num = 0
    biker = 0
    ped = 0
    cart = 0
    car = 0
    bus = 0
    skate = 0
    # $B%G%#%l%/%H%jKh$K%G!<%?$H2hA|$rFI$_9~$`(B
    for p in data_path:
        data = np.genfromtxt(p + 'annotations4.txt', delimiter=' ')
        unique_id = np.unique(data[:, 0])
        num += len(unique_id)
        # $B3JG<$9$kG[Ns$rMQ0U(B
        save_array = np.empty((0, 10), dtype=np.int32)
        # $B%G!<%?%;%C%H$N(BID$BKh$KFI$_9~$`(B
        for id in unique_id:
            data_id = data[data[:, 0] == id, 9]
            uni = np.unique(data_id)
            if uni == 1:
                biker += 1
            elif uni == 2:
                ped += 1
            elif uni == 3:
                cart += 1
            elif uni == 4:
                car += 1
            elif uni == 5:
                bus += 1
            else:
                skate += 1
    print(("$BA4It(B",num))
    print(("biker",biker))
    print(("ped",ped))
    print(("cart",cart))
    print(("car",car))
    print(("bus",bus))
    print(("skate",skate))


if __name__ == '__main__':
    main()
