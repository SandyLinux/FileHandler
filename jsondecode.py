import json
dictstr = '["foo", {"bar":["baz", null, 1.0, 2]}]'
mylist = json.loads(dictstr)

print(mylist, 'type is ', type(mylist))
print(mylist[1]['bar'][2])

mydict= {'header':'h1', 'body':'this is a new line'}

mystr=json.dumps(mydict)

print(mystr)


mydict2 = json.loads(mystr)
print(mydict2, '----',type(mydict2))
print(mydict2['header'])
print(mydict2['body'])

data = 'new line \n\n\n\t\tother line'
print(data)
print('---')
with open('1','w') as f:
	f.write(data)

data1 = 'He said, \t\'I will come tomorrow\'\nthen he left home\nwill he be there?'
print(data1)
print('---')
with open('1','w') as f:
	f.write(data1)
