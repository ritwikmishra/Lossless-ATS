# -*- coding: utf-8 -*-
import unicodedata
import glob

cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))
ck = len(cnnfiles)
slen = 0.0
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/dml_toks/"+str1[34:]
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	t1 = sum(sum(len(k) for k in i.split()) for i in hypo)
	t2 = sum(sum(len(k) for k in i.split()) for i in ref)
	try:
		t3 = t1/float(t2)
	except:
		ck-=1
		print "Division error"
		k+=1
		continue
	slen += t3
	# print cnnfiles[k]
	# print t1, t2, t3
	print str(k)+"/"+str(ck)
	k+=1
	# break

file = open("/home/ritwik/ATS/dataset/length.txt","a")
file.write("mysummary vs dml_toks\n"+str(slen/ck)+"\n\n")
file.close()