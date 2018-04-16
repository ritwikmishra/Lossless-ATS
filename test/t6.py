import time
import threading
import sys
import random
import re

def gettabs (str1):
	ts = len(str1) - len(str1.lstrip('	'))
	return ts

def getparent (content, j):
	k = gettabs(content[j])
	#print k
	if k==0:
		return ["END",-1]
	while "# ::" not in content[j-1]:
		if gettabs(content[j-1]) == k-1:
			kk = content[j-1].find('(')
			return [content[j-1][kk:],j-1]
		j=j-1

def getVar(str1):
	k = str1.find(':')
	if k==-1:
		k=0
	else:
		while(k!=len(str1)-2 and str1[k]!=' '):
			k+=1
	k+=1
	if str1[k]=='(':
		k+=1
	kk = k 
	while(kk!=len(str1) and str1[kk]!=' '):
		kk+=1
	# print str1[k:kk],k,kk, len(str1)
	if re.findall(r'.*\d+',str1[k:kk].strip()):
		return str1[k:kk].strip()
	else:
		return "NA"

def removeDuplicates(content):
	myset = set()
	k=0
	while k<len(content):
		x=content[k]
		if "# ::id" in x:
			myset.clear()
		vr = getVar(x)
		if vr != "NA" and re.findall(r'[a-z]',vr):
			# print vr
			a = len(myset)
			myset.add(vr)
			b = len(myset)
			if (a==b):
				print vr, x, k
				gp = getparent(content, k)
				pvr = getVar(gp[0])
				print pvr, gp[0]
				pvr = re.findall(r'[0-9]+',pvr)[0]
				cvr = re.findall(r'[0-9]+',vr)[0]
				kk = x.find(cvr)
				tx = x[:kk] + pvr + x[kk+len(cvr):]
				print tx, pvr, cvr
				content[k] = tx
		k+=1

	for x in content:
		print x

	for x in content:
		if "# ::id" in x:
			myset.clear()
		vr = getVar(x)
		if vr != "NA":
			a = len(myset)
			myset.add(vr)
			b = len(myset)
			if (a==b):
				gp = getparent(content, content.index(x))
				cvr = re.findall(r'[0-9]+',vr)[0]
				kk = x.find(cvr)
				pvr = str(content.index(x))
				tx = x[:kk] + pvr + x[kk+len(cvr):]
				content[content.index(x)] = tx
	return content


file = open("summ.txt","r")
content=[x.rstrip('\n') for x in file.readlines() if x.strip()]
content = removeDuplicates(content)

for x in content:
	print x

# k = random.randint(1,8)
# time.sleep(k)
# print k
# print "Done!"