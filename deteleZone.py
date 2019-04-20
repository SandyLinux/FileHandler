import os
def DeleteZone(Zone): #Delete a zone and the information contained within named.conf.local and lanaware.com.zone
	flag = 0
	File = open("local", "r+")
	tmpsave = open("tmpsave", "a")
	for i in File.readlines():
		if i.startswith("zone \"" + Zone):
			print("start with zone---", i)
			flag = 1
		if flag > 0 and flag < 7:
			flag += 1
		else:
			tmpsave.write(i) 
	File.close()
	tmpsave.close()

	os.system("mv tmpsave local")

	flag = 0
	File = open("lanaware", "r+")
	tmpsave = open("tmpsave", "a")
	for i in File.readlines():
		if i.startswith(Zone):
			print('werwer')
			flag += 1
		if flag > 0 and flag < 3:
                        flag += 1
		else:
			tmpsave.write(i)
	File.close()
	tmpsave.close()
	os.system("mv tmpsave lanaware")

DeleteZone('n4')
