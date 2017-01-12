import hashlib

#sha1
p1 = open("pw1.hex", "r").read()
#sha256
p2 = open("pw2.hex", "r").read()
#md5
p3 = open("pw3.hex", "r").read()
#salt
slt = open("salt.hex", "r").read()

#sha256
sp1 = open("spw1.hex", "r").read()
#md5
sp2 = open("spw2.hex", "r").read()
#sha1
sp3 = open("spw3.hex", "r").read()


pw1 = int(p1,16)
pw2 = int(p2,16)
pw3 = int(p3,16)
salt = int(slt, 16)
spw1 = int(sp1, 16)
spw2 = int(sp2, 16)
spw3 = int(sp3, 16)



def getRegularPasswords():
	with open("dic-0294.txt") as pFile:
		for line in pFile:
			
			sha1Val = int(hashlib.sha1(line.strip()).hexdigest(),16)
			sha256Val = int(hashlib.sha256(line.strip()).hexdigest(),16)
			md5Val = int(hashlib.md5(line.strip()).hexdigest(),16)
			if(sha1Val==pw1):
				print "Found pw1"
				print "pw1 is: " + line
			if(sha256Val==pw2):
				print "Found pw2"
				print "pw2 is: " + line
			if(md5Val==pw3):
				print "Found pw3"
				print "Pw3 is: " + line


def getSaltedPasswords(s):
	with open("dic-0294.txt") as pFile:
		count = 0
		for line in pFile:
			sha1Val1 = int(hashlib.sha1(line.strip() + s).hexdigest(),16)
			sha256Val1 = int(hashlib.sha256(line.strip() + s).hexdigest(),16)
			md5Val1 = int(hashlib.md5(line.strip() + s).hexdigest(),16)
			#print sp1
			sha1Val2 = int(hashlib.sha1(s+line.strip()).hexdigest(),16)
			sha256Val2 = int(hashlib.sha256(s+line.strip()).hexdigest(),16)
			md5Val2 = int(hashlib.md5(s+line.strip()).hexdigest(),16)
			#print sha1Val1
			#print sha1Val2
			if(sha256Val1==spw1 or sha256Val2==spw1):
				print "Found spw1"
				print "spw1 is: " + line
			if(md5Val1==spw2 or md5Val2==spw2):
				print "Found spw2"
				print "spw2 is: " + line
			if(sha1Val1==spw3 or sha1Val2==spw3):
				print "Found spw3"
				print "spw3 is: " + line
			count=count+1
			
def getSalt():
	newSalt = ""
	with open("dic-0294.txt") as pFile:
		for line in pFile:
			md5Val = int(hashlib.md5(line.strip()).hexdigest(),16)
			sha1Val = int(hashlib.sha1(line.strip()).hexdigest(),16)
			sha256Val = int(hashlib.sha256(line.strip()).hexdigest(),16)
			if(salt==md5Val):
				print "Found salt"
				print line
				newSalt = salt
			if(salt==sha1Val):
				print "Found salt"
				print line
				newSalt = salt
			if(salt==sha256Val):
				print "Found salt"
				print line
				newSalt = salt
	return str(newSalt)


#getRegularPasswords()
s = getSalt()
getSaltedPasswords(s)
print hashlib.md5("").hexdigest()
	

