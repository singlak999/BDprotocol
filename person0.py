import person1
import person2
import subprocess
import threading
import Public
class Self:
	def __init__(self):
		self.e=1
s=Self()
lock=threading.Lock()
with open('Public.py','a') as f:
	f.write('ge0=2')
lock.acquire()
try:
	print(subprocess.check_output(['python', f'person1']))
finally:
	lock.release()
pg=Public.g2
pn=Public.g1
r=((pg/pn)**s.e)%11
with open('Public.py','a') as f:
	f.write('r0=r')
key=pg**(3*s.e)
for i in range(0,3):
	key*=Public.r2
print(key)