import person0
import person1
import subprocess
import threading
import Public
class Self:
	def __init__(self):
		self.e=7
s=Self()
lock=threading.Lock()
with open('Public.py','a') as f:
	f.write('ge2=128')
pg=Public.g1
pn=Public.g0
r=((pg/pn)**s.e)%11
with open('Public.py','a') as f:
	f.write('r2=r')
key=pg**(3*s.e)
for i in range(0,3):
	key*=Public.r1
print(key)