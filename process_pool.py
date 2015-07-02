from multiprocessing import Pool
import os,time,random

def long_time_task(name):
	print 'Run task %s (%s)...' % (name,os.getpid())
	start = time.time()
	time.sleep(random.random() * 3)
	end = time.time()
	print 'Task %s runs %0.2f seconds.' % (name,(end-start))

if __name__ == '__main__':
	print 'parent process %s.' % os.getpid()
	p = Pool()
	for i in range(20):
		p.apply_async(long_time_task, args=(i,))
	print 'Waiting for all subprocess done...'
	p.close()
	p.join()
	print 'All subprocess done.'
