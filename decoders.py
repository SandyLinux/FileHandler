from multiprocessing import Process
import sys,os
import time

def get_pname(pid):
    return os.system("ps -ef |grep {}".format(pid))

def say_hello(name='world'):
    print ("Hello, %s" % name)
    print ('Starting:', p.name, p.pid)
    sys.stdout.flush()
    print ('Exiting :', p.name, p.pid)
    sys.stdout.flush()
    time.sleep(3)

print ('main Starting:', os.getpid(), get_pname(os.getpid()))

p = Process(target=say_hello)
p.start()
print ('main ending:', os.getpid(),get_pname(os.getpid()))


string = 'pythön!'

# print string
print('The string is:', string)

# ignore error
print('The encoded version (with ignore) is:', string.encode("utf-8"))

import pdb
#pdb.set_trace()
encoderet = string.encode("ascii", 'replace')
decoderet = encoderet.decode('ascii')

# replace error
print('The encoded version (with replace) is:', string.encode("ascii", "replace"))
