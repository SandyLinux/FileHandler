
data = 'new line \n\n\n\t\tother line'
print(data)
print('---')
with open('1','w') as f:
	f.write(data)

data1 = 'He said, \'I will come tomorrow\'\nthen he left home\nwill he be there?'
print(data1)
print('---')
with open('1','w') as f:
	f.write(data1)


path = 'c:\new folder'
path1 = r'c:\new folder'
print(path,'\n',path1)

body=('erewrewrwrewrwr'
	'ewrwerwe'
	'111111'
	'444444'
	'666666')
mytuple=('2323',)
print(body, type(body))
print(mytuple, type(mytuple))
