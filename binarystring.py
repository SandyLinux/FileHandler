binstr=b'message'

mystr1 = binstr.decode('utf-8')
print(mystr1)
print(binstr)

binseq = '0110100001101001'

print(chr(int(binseq[:8],2)))

def binary_decode_string(s, encoding='utf-8'):
	#a = list( chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
	a = ''.join( chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
	return a.encode(encoding)


a = binary_decode_string(binseq)
print(a)


mydict={'name':'zhang','id':1001,'address':'1 main street'}

mystring =''.join(str(k)for k in (mydict.values()))
print(mystring)
