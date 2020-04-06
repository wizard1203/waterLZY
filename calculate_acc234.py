import os



class AverageMeter(object):
    """Computes and stores the average and currentcurrent value"""
    def __init__(self):
        self.reset()

    def reset(self):
        self.val = 0
        self.avg = 0
        self.sum = 0
        self.count = 0

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count


def accuracy(output, target):
	accs = {}
	for i, i_output in enumerate(output):
		if i_output == target:
			for j in range(i, 5):
				accs[j+1] = 1
			break
		else:
			accs[i+1] = 0

	return accs



if __name__ == '__main__':

	filePath = "..//exp_results//exp_results"
	acc234_path = os.path.join(filePath, "acc234.txt")
	files = os.listdir(filePath)
	acc234 = open(acc234_path, 'w')
	for file in files:
		acc234.write(file)
		acc234.write('\n')
		file = os.path.join(filePath, file)
		print(file)
		accs_ave = {}
		for i in range(5):
			accs_ave[i+1] = AverageMeter()
		flog = open(file, 'r')
		for line in flog.readlines():
			line = line.split(',')
			line = [i.strip() for i in line]
			if len(line) != 11:
				break
			accs = accuracy(line[0:5], line[10])
			for i, acc in accs.items():
				accs_ave[i].update(acc)
		for i in range(5):
			acc234.write('acc{0}:{1.avg}'.format(i+1, accs_ave[i+1]))
			acc234.write('\n')
		print('acc{0}:{1.avg}'.format(i, accs_ave[i]))


		flog.close()
	acc234.close()




