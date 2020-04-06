import os

import numpy as np
import logging
from config import opt
def read_sample(sample_file_path):
    """Returns the sample_file.

    Args:
        sample_file (file): The file of the sample.

    Returns:
        a data sample

    """ 
    with open(sample_file_path, 'r') as f:
        lines = f.readlines()
        # label = int(float(lines[0].split(',')[0].strip()))
        if opt.multi_label > 1:
            reallabel = [int(float(item.strip())) for item in lines[0].split(',')[0:opt.multi_label]]
            label = [0]*len(opt.labels_dict)
            #print(label)
            for single_label in reallabel:
                if single_label != 0:
                    label[opt.labels_dict.index(single_label)] = 1
            datas = [(float(item)) for item in lines[0].split(',')[opt.multi_label:-1]]
        else:
            reallabel = int(float(lines[0].split(',')[0].strip()))
            label = opt.labels_dict.index(reallabel)
            datas = [(float(item)) for item in lines[0].split(',')[1:-1]]
        # print(lines[0])
        #print(len(datas))
        #print("===========\n")
        #print(datas[100])
        #print(datas)
# for line in lines[1:] :
        #     line = [float(item) for item in line.split(',')]
        #     datas.append(line)
    f.close()
    return label, datas



class WaterDataset:

    def __init__(self, data_dir, num_of_samples='default', split='train'):
        self.data_dir = os.path.join(data_dir, split)
        if num_of_samples == 'default':
            self.list_file = os.listdir(self.data_dir)
        else:
            #num_of_samples = int(num_of_samples)
            self.list_file = os.listdir(self.data_dir)[0:num_of_samples]

    def __len__(self):
        return len(self.list_file)

    def get_example(self, i):
        """Returns the i-th sample.

        Args:
            i (int): The index of the sample_files.

        Returns:
            a data sample

        """
        # Load a sample
        sample_file = self.list_file[i]

        label, datas = read_sample(os.path.join(self.data_dir, sample_file))
        return label, datas

    __getitem__ = get_example


