import os

if __name__ == '__main__':

	filePath = "..//exp_results200115_convergence//log"
	conver_file_path = os.path.join(filePath, "log_self_waterdsnetf_SGD200115_LeakScale_M6_lr_0.6_num_of_samples_default.log")
	conver_file = open(conver_file_path, 'r')
	acc1s = []
	acc5s = []
	for line in conver_file.readlines():
		if line.find('validate') != -1:
			print(line)
			line = line.split('Acc@1')[1]
			line = line.split()
			acc1 = line[0].strip()
			acc5 = line[2].strip()
			acc1s.append(float(acc1))
			acc5s.append(float(acc5))
	print(acc1s)
	print(acc5s)
	conver_file.close()

	conver_write_file_path = os.path.join(filePath, "log_self_waterdsnetf_SGD200115_LeakScale_M6_lr_0.6_num_of_samples_default_with_epoch.log")
	conver_write_file = open(conver_write_file_path, 'w')
	conver_write_file.write(str(acc1s))
	conver_write_file.write('\n')
	conver_write_file.write(str(acc5s))
	conver_write_file.close()
	# acc234_path = os.path.join(filePath, "acc234.txt")
	# files = os.listdir(filePath)
	# acc234 = open(acc234_path, 'w')
	# for file in files:
	# 	acc234.write(file)
	# 	acc234.write('\n')
	# 	file = os.path.join(filePath, file)
	# 	print(file)
	# 	accs_ave = {}
	# 	for i in range(5):
	# 		accs_ave[i+1] = AverageMeter()
	# 	flog = open(file, 'r')
	# 	for line in flog.readlines():
	# 		line = line.split(',')
	# 		line = [i.strip() for i in line]
	# 		if len(line) != 11:
	# 			break
	# 		accs = accuracy(line[0:5], line[10])
	# 		for i, acc in accs.items():
	# 			accs_ave[i].update(acc)
	# 	for i in range(5):
	# 		acc234.write('acc{0}:{1.avg}'.format(i+1, accs_ave[i+1]))
	# 		acc234.write('\n')
	# 	print('acc{0}:{1.avg}'.format(i, accs_ave[i]))


	# 	flog.close()
	# acc234.close()










