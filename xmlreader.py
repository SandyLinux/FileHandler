from xml.dom import minidom
doc = minidom.parse('/Users/sandy/Documents/GitHub/test/plant_catalog.xml')

# doc.getElementsByTagName returns NodeList

staffs = doc.getElementsByTagName("PLANT")
for staff in staffs:
        sid = staff.firstChild.nodeValue
        #nickname = staff.getElementsByTagName("nickname")[0]
        #salary = staff.getElementsByTagName("salary")[0]
        print(sid)
