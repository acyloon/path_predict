# coding:UTF-8
import numpy as np
import os
from glob import glob
from norm import train

'''---------------------------'''
PATH = '../../SDD_data/train/*/*/'
'''---------------------------'''

class Train_DataLoader():
    '''
    :return
    all_data        :Target data for all scenes
    list_coordinate :Target in all scenes divides by list
    list            :Number of target per scene
    '''
    def __init__(self, sequence=5):
        self.scene = glob(PATH)
        self.scene.sort()

        self.sequence = sequence
        self.list = []
        self.list_coordinate = []
        self.all_data = []

        for i, j in zip(self.scene, list(range(len(self.scene)))):
            self.out = []
            data_split = []
            print(i, "----------------------------")
            print(j)
            sub_path = os.path.join(i, "annotations4.txt") # change _ to 4
            data = np.genfromtxt(sub_path, delimiter=' ')
            # Center coordinates from Bounding Box
            x_lim1, y_lim1 = data[:, 1], data[:, 2]
            x_lim2, y_lim2 = data[:, 3], data[:, 4]
            x = (x_lim1 + x_lim2) // 2
            y = (y_lim1 + y_lim2) // 2

            # Normalization
            x, y = train(x, y, j)
            data[:, 1], data[:, 2] = x, y

            # all target in the scene
            ID = np.unique(data[:, 0][-1])
            for k in range(0, int(ID[0])):
                trajectory = data[data[:, 0] == k, :]
                # ID,x,y,frame
                trajectory = trajectory[:, [0, 1, 2, 5]]
                if len(trajectory) > 0:
                    data_split.append(trajectory)

            for split in range(len(data_split)):
                data_split_coor = data_split[split]
                if data_split_coor.shape[0] > self.sequence + 1:
                    self.out.append(data_split_coor[:, [1, 2]])
                    self.all_data.append(data_split_coor[:, [1, 2]])

            self.list_coordinate.append(self.out)
            self.list.append(len(self.out))
