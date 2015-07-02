import random, time, Queue
from multiprocessing.managers import BaseManager
##queue of transmitting task
task_queue = Queue.Queue()
##queue of receiving task
result_queue = Queue.Queue()

##QueueManager inherit from Basemanager
class QueueManager(BaseManager):
	pass

##register the two queue on the internet,parameter callable associated with the object queue
QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)
#bind to port 5000,set security code as 'abc'
manager = QueueManager(address=('',5000), authkey='abc')
##start Queue
manager.start()
#get object Queue visited by Internet
task = manager.get_task_queue()
result = manager.get_result_queue()
##put serveral tasks in 
for i in range(10):
	n = random.randint(0,10000)
	print('Put task %d...' % n)
	task.put(n)

print('Try get results...')
#read result frome queue result
for i in range(10):
	r = result.get(timeout=10)
	print('Result:%s' % r)
##shut down
manager.shutdown()
