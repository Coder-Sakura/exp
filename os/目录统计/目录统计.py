import os,datetime
 
def get_dir_size(dir):
    size = 0
    a = datetime.datetime.now()
    for root, dirs, files in os.walk(dir,topdown =False):
        size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
    b = datetime.datetime.now()
    print('扫描时间为: {}s'.format((b-a).seconds))
    return size
 
if __name__ == '__main__':
	size = get_dir_size('test')
	if size/1024/1024 > 1024:
		print('Total size is: %.3f Gb'%(size/1024/1024/1024))
	else:
		print('Total size is: %.3f Mb'%(size/1024/1024))