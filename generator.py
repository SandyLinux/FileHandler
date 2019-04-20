def gen():
	for x in range(1,6):
    		yield x


mylist = list(x for x in gen())
import ipdb

#ipdb.set_trace()
g1 = gen()
text = 'haha'+'jojo'
mylst = range(10,20)


def numberGen(n):
	num = 0
	while num < n:
		yield num
		num +=1


numberlist=numberGen(5)
try:
	while True:
		print(next(numberlist))
except StopIteration as e:
	print('generate a stop iteration error',e)


'''
several tools:
1. next()
2. yield()
3. send(), ；
'''
