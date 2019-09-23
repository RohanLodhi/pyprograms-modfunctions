import time

stime=time.time()
print(time.ctime(stime))
print('before execution')

for i in range(1,11):
	time.sleep(1)
	print(i)
print('after execution')	
etime=time.time()
print(time.ctime(etime))

