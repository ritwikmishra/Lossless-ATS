import re 
import sys
import os
import nltk
from pywsd.lesk import simple_lesk

def gettabs (str1):
	ts = len(str1) - len(str1.lstrip('	'))
	return ts

def gettag (str1):
	k = str1.find(':')
	l = str1.find('(')
	return str1[k+1:l-1]

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

def getInstance (str1):
	k = str1.find(':')
	if k==-1:
		return str1[1:]
	while str1[k] != ' ' and k!=len(str1)-2:
		k+=1
	return str1[k+1:]

def getword (str1):
	t = str1.rfind(' ')
	return str1[t:].strip()


def graphMerge(content, i, j, windx1, windx2): #bydefault FALL
	
	ti=i
	tj=j

	#uncomment this to get RISE
	# tmp1 = i
	# i = j
	# j = tmp1
	# ti = i
	# tj = j
	# tmp1 = windx1
	# windx1 = windx2
	# windx2 = tmp1

	# print ("i = "+str(i)+" j = "+str(j))
	str1 = "x"+str(windx2)+" "
	#print ("#### 15"+content[15])

	i+=1
	#find that word in below amr; stored in i 
	while str1 not in content[i]:
		if "# ::tok" in content[i] or i==len(content)-1:
			print ("ERROR! below")
			# print str1
			return ["empty"]
			# exit()
		i+=1

	str1 = "x"+str(windx1)+" "

	j+=1
	#find that word in above amr (this will check for xNumber followed by a space i.e. "x21 ")
	while str1 not in content[j]:
		if "# ::tok" in content[j] or j==len(content)-1:
			print ("ERROR! above")
			# print (str1+"#")
			# qj=tj+1
			# while "#" not in content[qj]:
			# 	print content[qj]
			# 	qj+=1
			return ["empty"]
			# exit()
		j+=1

	#check if those words have common parent or sibling or children
	tvar = gettabs(content[j])
	mylist1 = []
	tp1 = getparent(content,j)
	# print getword(tp1[0])
	mylist1.append(getword(getparent(content,j)[0])) #parent
	tt1 = 1
	while gettabs(content[j+tt1])==tvar+1: 
		mylist1.append(getword(content[j+tt1])) #children
		tt1+=1
	tt1 = 1
	while gettabs(content[tp1[1]+tt1]) == tvar:
		if (tp1[1]+tt1 != j):
			mylist1.append(getword(content[tp1[1]+tt1])) #sibling
		tt1+=1
	# print mylist1

	tvar = gettabs(content[i])
	mylist2 = []
	tp1 = getparent(content,i)
	# print getword(tp1[0])
	mylist2.append(getword(getparent(content,i)[0])) #parent
	tt1 = 1
	while i+tt1 < len(content) and gettabs(content[i+tt1])==tvar+1: 
		mylist2.append(getword(content[i+tt1])) #children
		tt1+=1
		if i+tt1 == len(content):
			break
	tt1 = 1
	# print tp1[1]+tt1, len(content)
	while tp1[1]+tt1 < len(content) and gettabs(content[tp1[1]+tt1]) == tvar:
		if (tp1[1]+tt1 != i):
			mylist2.append(getword(content[tp1[1]+tt1])) #sibling
		tt1+=1
		if tp1[1]+tt1 == len(content):
			break
	# print mylist2

	if len(set(mylist1).intersection(mylist2)) == 0:
		print "No similarity found for "+getword(content[j])
		return ["empty"]

	# print ("Index of the below line containing given word "+str(i))
	# print content[ti] #below
	# print ("Index of the above line containing given word "+str(j))
	# print content[tj] #above
	#print (len(content[tj].split())-2)
	
	#adding bias to the below tokens
	#uncomment this (and line 98) to get RISE
	# tj, ti = ti, tj
	bias = len(content[tj].split())-2
	k=ti+1
	while k < len(content) and "#" not in content[k]:
		if re.match(".*\([a-z][0-9].*",content[k]):
			kt = content[k].find('/')
			kp = content[k].find('(')
			if kt == -1 or kp ==-1:
				kq = content[k].find(' x')+1
				nn = int(content[k][kq+1:].lstrip())
				kp = kq-1
				kt = len(content[k])+1
			else:
				#print content[k][kp+2:kt-1]
				nn = int(content[k][kp+2:kt-1])
			nn = nn + bias
			content[k] = content[k][:kp+2] + str(nn) + content[k][kt-1:]
		elif "(xap" in content[k]:
			kt = content[k].find('/')
			kp = content[k].find('(')
			nn = int(content[k][kp+4:kt-1])
			nn = nn + bias
			content[k] = content[k][:kp+4] + str(nn) + content[k][kt-1:]
		k+=1
	# tj, ti = ti, tj

	#getting parents and merging 
	nlist = []
	nlist.append(content[i])
	nj = j
	gp = getparent(content,nj)
	ts = gettabs(content[i])
	# print ("@@@@ "+content[j])
	while gp[1] != -1:
		str1 = gettag(content[nj])+"-of "+gp[0]
		ts+=1
		str1 = "	" * ts + ":" + str1
		str1 = str1.replace('-of-of','')
		# print "#############"
		# print str1
		# print "#####"
		nlist.append(str1)
		# print gp
		nj = gp[1] #parent original
		nntb = gettabs (content[nj]) #tabs in parent
		nnj = nj+1 #child
		
		while gettabs(content[nnj])>nntb: #tabs in child > tabs in parent
			if gettabs(content[nnj]) == nntb + 1: #if child is exact child of parent
				# print ("Child is == "+content[nnj])
				flag = False
				for x in nlist:
					if getInstance(content[nnj]) in x or nnj == j:
						flag = True
						break
				if flag == False:
					str1 = "	"*(ts+1) + content[nnj].lstrip()
					nlist.append(str1)
					nnj+=1
					while gettabs(content[nnj])>nntb+1:
						str1 = "	" * (ts+1+(gettabs(content[nnj])-nntb-1)) + content[nnj].lstrip()
						nlist.append(str1)
						nnj+=1
					if gettabs(content[nnj])<=nntb+1:
						nnj-=1
			nnj+=1
		gp = getparent(content,nj)
		#print "here"

	#adding sibling leaves (the leftover nodes) and their properties 
	#actually adding offsprings of the J 
	# print "@NJ ", nj, content[nj]
	while nj < len(content) and "#" not in content[nj]:
		wrd = getInstance(content[nj])
		# wrd = content[nj][content[nj].find(' '):] #extracting answer="x21 / word" from str="	:ARG1 (x21 / word"
		flag = False
		for x in nlist:
			if wrd in x:
				flag = True
				break
		if flag == False and nj!=j:
			# print "@HERE ===== ", wrd
			wrd2 = getparent(content,nj)

			wrd2n = wrd2[1] 
			wrd2 = wrd2[0]
			# wrd2 = wrd2t[wrd2t.find(' '):]
			if wrd2n == j:
				wrd2 = getInstance(content[i])  
			# print ("##"+wrd2)
			# print "@parent ------", wrd2
			for x in nlist:
				if wrd2 in x:
					k = gettabs(x)
					str1 = "	" * (k+1) + content[nj].lstrip('	')
					#print str1
					nlist.append(str1)
					break
		nj+=1

	ii=i
	# if ti+1 == ii:
	# 	ii+=1
	ti2 =ti
	while "# ::id" not in content[ti2]:
		ti2+=1
		if ti2 == len(content) -1:
			ti2+=1
			break
	#print ti2
	nlist = content[ti+1:ii]+nlist+content[i+1:ti2]
	# print ("$$$ "+nlist[len(nlist)-1])

	#bracket balancing
	k = 0
	br = 0
	while k<len(nlist)-1:
		if "(" in nlist[k]:
			if gettabs(nlist[k+1]) <= gettabs(nlist[k]):
				nlist[k] = nlist[k] + ")"*(gettabs(nlist[k])-gettabs(nlist[k+1])+1)
				br = br - (gettabs(nlist[k])-gettabs(nlist[k+1]))
			else:
				br+=1
		else:
			if gettabs(nlist[k+1]) < gettabs(nlist[k]):
				nlist[k] = nlist[k] + ")"*(gettabs(nlist[k])-gettabs(nlist[k+1]))
				br = br - (gettabs(nlist[k])-gettabs(nlist[k+1]))
		k+=1
	if "(" in nlist[len(nlist)-1]:
		br+=1
	nlist[len(nlist)-1] = nlist[len(nlist)-1] + ")"*(br) 

	#uncomment this to get RISE
	# tmp1 = ti
	# ti = tj
	# tj = tmp1

	#adding the ::snt and ::tok
	tl = []
	tl.append(content[tj-2])
	tl.append(content[tj-1]+content[ti-1][7:])
	tl.append(content[tj] + content[ti][7:])

	nlist = tl + nlist

	# for x in nlist:
	# 	print x


	nlist = addIndex(nlist)


	# for x in nlist:
	# 	print x

	# print "+"*200

	return nlist

def addIndex(nlist):
	k=0
	while k<len(nlist):
		if re.match(".*\([a-z] .*", nlist[k]):
		# if "(n " in nlist[k]:
			gp = getparent(nlist, k)
			if gp[0]=="END":
				k+=1
				continue
			nos = re.findall(r'x\d+',gp[0]) #list of x[0-9]+
			if (len(nos)==0):
				gp = getparent(nlist, gp[1])
				nos = re.findall(r'x\d+',gp[0])
				if len(nos)==0:
					gp = getparent(nlist, gp[1])
					nos = re.findall(r'x\d+',gp[0])
			tnum = int(nos[0][1:])
			npmetc = re.findall(r'\([a-z] ',nlist[k])[0]
			nlist[k] = nlist[k][:nlist[k].find(npmetc)+2]+str(tnum)+nlist[k][nlist[k].find('/')-1:]

		if "(xap" in nlist[k]:
			gp = getparent(nlist,k)
			if gp[0]=="END":
				k+=1
				continue
			nos = re.findall(r'x\d+',gp[0]) #list of x[0-9]+
			if (len(nos)==0):
				gp = getparent(nlist, gp[1])
				nos = re.findall(r'x\d+',gp[0])
				if len(nos)==0:
					gp = getparent(nlist, gp[1])
					nos = re.findall(r'x\d+',gp[0])
			tnum = int(nos[0][1:])
			nlist[k] = nlist[k][:nlist[k].find("(xap")+4] + str(tnum) + nlist[k][nlist[k].find('/')-1:]
		k+=1
	return nlist
	

def getCommonWord(str1, str2):
	# str1 = "Some scoff at the notion that movies do anything more than entertain ."
	# str2 = "Some are wrong ."
	ml1 = str1.lower().split()
	ml1 = ml1[2:]
	ml1[0] = ml1[0][0].upper() + ml1[0][1:]
	ml2 = str2.lower().split()
	ml2 = ml2[2:]
	ml2[0] = ml2[0][0].upper() + ml2[0][1:]
	print ml1 
	print ml2
	ml3 = set(ml1).intersection(ml2)
	# print ml3
	file = open("stpwrds.txt", "r+")
	stpwrds=[x.rstrip('\n').rstrip(')') for x in file.readlines() if x.strip()]
	file.close()
	ml4 = set(ml3).difference(stpwrds)
	# print ml4
	ml4 = list(ml4)
	print ml4
	i=0
	while i<len(ml4):
		if simple_lesk(str1,ml4[i]) != simple_lesk(str2,ml4[i]):
			del ml4[i]
		i+=1

	t2 = nltk.pos_tag(ml4)
	ml = []
	for x in t2:
		if x[1][0] == 'V':
			ml.append(x[0])
	for x in t2:
		if x[1][0] == 'N':
			ml.append(x[0])
	for x in t2:
		if x[1][0] == 'P' and x[1][1]=='R':
			ml.append(x[0])
	for x in t2:
		if x[1] == "CD":
			ml.append(x[0])
	for x in t2:
		if x[1][0] == 'F':
			ml.append(x[0])
	for x in t2:
		if x[0] not in ml:
			ml.append(x[0])
	# print t2
	# print ml

	print "After WSD and POS reordering:\n", ml
	i=0
	while i<len(ml):
		ml[i]=ml[i].lower()
		i+=1

	return ml

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

	if "::id" in str1 or "::snt" in str1 or "::tok" in str1:
		return "NA"

	if re.findall(r'.*\d+',str1[k:kk].strip()) and re.findall(r'[a-z]',str1[k:kk].strip()):
		return str1[k:kk].strip()
	else:
		return "NA"

def removeDuplicates(content):
	myset = set()
	k=0
	while k<len(content):
		x = content[k]
		if "# ::id" in x:
			myset = set()
		vr = getVar(x)
		if vr != "NA":
			a = len(myset)
			myset.add(vr)
			b = len(myset)
			if (a==b):
				gp = getparent(content, k)
				pvr = getVar(gp[0])
				try:
					pvr = re.findall(r'[0-9]+',pvr)[0]
				except:
					print pvr, gp, content[k], vr
					exit()

				cvr = re.findall(r'[0-9]+',vr)[0]
				kk = x.find(cvr)
				# pvr = str(content.index(x))
				tx = x[:kk] + pvr + x[kk+len(cvr):]
				content[k] = tx
		k+=1

	# for x in content:
	# 	print x
	k=0
	while k<len(content):
		x = content[k]
		if "# ::id" in x:
			myset = set()
		vr = getVar(x)
		if vr != "NA":
			a = len(myset)
			myset.add(vr)
			b = len(myset)
			if (a==b):
				gp = getparent(content, k)
				cvr = re.findall(r'[0-9]+',vr)[0]
				kk = x.find(cvr)
				pvr = str(k)
				tx = x[:kk] + pvr + x[kk+len(cvr):]
				content[k] = tx
		k+=1
	return content
	

file = open("art.txt","r+")
file2 = open("summ.txt","w")
#content=[x.rstrip() for x in file.readlines() if x.strip()]
content=[x.rstrip('\n') for x in file.readlines() if x.strip()]
content = addIndex(content)
content2 = []
for x in content:
	content2.append(x.rstrip(')'))

i=j=k=0


while k<len(content):
	if "::tok" in content[k] and j==0 and i==0:
		j=k
	elif "::tok" in content[k] and j!=0 and i==0:
		i=k
	if i!=0 and j!=0:
		mystr1 = ""
		if "#LAST" in content[j-2]:
			mystr1 = content[j-2][8:]
		else:
			mystr1 = content[j]
		cw = getCommonWord(content[i], mystr1)
		# print content[i]
		# print mystr1
		# print cw
		if len(cw) == 0:
			j=i
			i=0
			# print "Here"
		else:
			ml = list(cw)
			nlist = ["empty"]
			# if ml[0]=="bin":
			# print (content[i])
			# print (content[j])
			#print ("i ="+str(i)+" j="+str(j))

			# print windx1
			# print windx2
			# print i
			# print j
			# repeat for all common words
			while nlist[0] == "empty":
				if len(ml)==0:
					j=1
					i=0
					break
				print ml[0]
				if "::tok" in mystr1:
					windx1 = mystr1.lower().split().index(ml[0]) - 1 
				else: #LAST:- in mystr1, hence windx1 is above
					windx1 = mystr1.lower().split().index(ml[0]) + 1
					windx1 = windx1 + (len(content[j].split())-2 - len(mystr1.split()))
				windx2 = content[i].lower().split().index(ml[0]) - 1
				nlist = graphMerge(content2, i, j, windx1, windx2)
				if nlist[0]=="empty": #this common word not present
					ml = ml[1:]		  #take next common word
			if len(ml)==0:
				k+=1
				continue
			ti2 = i
			while "# ::id" not in content[ti2]:
				ti2+=1
				if ti2 == len(content) -1:
					ti2+=1
					break

			if "#LAST" in content[j-2]:
				content = content[:j-2] + ["#LAST:- "+content[i][8:]] + nlist[1:] + content[ti2:]
			else:
				content = content[:j-1] + ["#LAST:- "+content[i][8:]] + nlist[1:] + content[ti2:]
			content2 = []
			# print "\t\t\t\t\t#### TEMP ANSWER"
			for x in content:
				# print x
				content2.append(x.rstrip(')'))
			# sys.stdin.read(1)
			# os.system('clear')
			# os.system('clear')
			# os.system('clear')
			# print "#"*300
			# print "here"
			# print ""
			k=j-2
			i=j=0
			
	k+=1
print "################################################"

#check for duplicate variables
content = removeDuplicates(content)


for x in content:
	if "# ::id" in x and content.index(x)!=0:
		# print ""
		file2.write("\n")
	if "#LAST" not in x:
		file2.write(x+"\n")
	# print x

file2.close()
file.close()
