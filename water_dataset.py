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




class aaaDataset:

    def __init__(self, data_dir, num_of_samples='default', split='train'):
        self.data_dir = os.path.join(data_dir, "IN.txt")
        self.label_dir = os.path.join(data_dir, "OUT.txt")

        with open(self.data_dir, 'r') as f:
            lines = f.readlines()

            if num_of_samples == 'default':
                self.num_of_samples = len(lines)
            else:
                self.num_of_samples = num_of_samples
        f.close()

    def __len__(self):
        return self.num_of_samples

    def get_example(self, i, model='train'):
        """Returns the i-th sample.

        Args:
            i (int): The index of the sample_files.

        Returns:
            a data sample

        """
        # Load a sample
        if model=='train':
            i = i
        else:
            i = int(self.num_of_samples*0.0) + i

        with open(self.data_dir, 'r') as f_data:
            data = [ float(item) for item in f_data.readlines()[i].split()]
            #print(data)
            #print(len(data))
        f_data.close()
        with open(self.label_dir, 'r') as f_label:
            label = [ float(item) for item in f_label.readlines()[i].split()]
            #print(label)
            #print(len(label))
        f_data.close()

        return label, data

    __getitem__ = get_example


