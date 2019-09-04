# coding:UTF-8
# 手動でデータを選別するプログラム
import os
import numpy as np
from glob import glob

DATA = './*/*/'

def main():
    # 読み込むディレクトリ指定
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
    # ディレクトリ毎にデータと画像を読み込む
    for p in data_path:
        data = np.genfromtxt(p + 'annotations4.txt', delimiter=' ')
        unique_id = np.unique(data[:, 0])
        num += len(unique_id)
        # 格納する配列を用意
        save_array = np.empty((0, 10), dtype=np.int32)
        # データセットのID毎に読み込む
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
    print(("全部",num))
    print(("biker",biker))
    print(("ped",ped))
    print(("cart",cart))
    print(("car",car))
    print(("bus",bus))
    print(("skate",skate))


if __name__ == '__main__':
    main()
