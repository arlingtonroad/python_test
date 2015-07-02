
import time, sys , Queue
from multiprocessing.managers import BaseManager

#create similiar QueueManager
class QueueManager(BaseManager):
	pass

##because the QueueManager only get queue from Internet,it just provide name
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#connect to server,namely the machine running taskmanager.py
server_addr = '10.102.16.60'
print('Connect to server %s...' % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey='abc')

m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
	try:
		n = task.get(timeout=1)
		print('run task %d * %d...' % (n,n))
		r = '%d * %d = %d' % (n,n,n*n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('task queue is empty.')

print('worker exit.')
