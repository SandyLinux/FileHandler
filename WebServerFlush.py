def WebServerFlush(): #Flush all records within the given zone, it will look for "Flush Stopper" on where to stop.
	writer = "" 
	flag = False
	File = open("1.txt", "r+")
	Read = File.readlines() 
	for i in Read:
		if i.startswith(";Flush Stopper"):
			writer += ";Flush Stopper"
			break
		else:
			writer += i
	print(writer)
	File.seek(0)
	File.truncate()
	File.write(writer)
	File.close()

if __name__=='__main__':
	WebServerFlush()

