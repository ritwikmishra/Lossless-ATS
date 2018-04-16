import re

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

def getword (str1):
	k = str1.find('/')
	return str1[k+1:]

file = open("art.txt","r+")
#content=[x.rstrip() for x in file.readlines() if x.strip()]
content=[x.rstrip('\n').rstrip(')') for x in file.readlines() if x.strip()]

# pp = 0
# while pp<len(content):
# 	content[pp]=content[pp].lstrip(')')
# 	pp+=1

# print content


windx2 = 1 #index of common word in below
windx1 = 1 #index of common word in above

ti = i = 13 #index of tokenized sentence below
tj = j = 2  #index of tokenized sentence above

str1 = "x"+str(windx2)+" "

#print ("#### 15"+content[15])

i+=1
#find that word in below amr; stored in i 
while str1 not in content[i]:
	if "# ::tok" in content[i] or i==len(content)-1:
		print ("ERROR! below")
		# return ["empty"]
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
		# return ["empty"]
		# exit()
	j+=1

# print ("Index of the below line containing given word "+str(i))
# print content[i] #below
# print ("Index of the above line containing given word "+str(j))
# print content[j] #above
#print (len(content[tj].split())-2)

#adding bias to the below tokens
bias = len(content[tj].split())-2
k=ti+1
while k < len(content) and "#" not in content[k]:
	if re.match(".*x[0-9].*",content[k]):
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
	k+=1

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
				if getword(content[nnj]) in x or nnj == j:
					flag = True
					break
			if flag == False:
				str1 = "	"*(ts+1) + content[nnj].lstrip()
				nlist.append(str1)
				nnj+=1
				while gettabs(content[nnj])>nntb+1:
					str1 = "	" * (ts+1+(gettabs(content[nnj])-nntb-1)) + content[nnj].lstrip()
					# if "x2 / hostility" in content[nnj]:
						# print "\t\t\t\t@@@@@@@@@@@HERE@@@@@@@@@@@@@@@"
						# print ("	" * (ts+5+(gettabs(content[nnj])-nntb-1)) + content[nnj].lstrip())
						# print ("	" * (ts+2+(gettabs(content[nnj])-nntb-1)) + content[nnj].lstrip())
						# print ("	" * (ts+3+(gettabs(content[nnj])-nntb-1)) + content[nnj].lstrip())
						# print "\t\t\t\t@@@@@@@@@@@HERE@@@@@@@@@@@@@@@"
					nlist.append(str1)
					nnj+=1
				if gettabs(content[nnj])<=nntb+1:
					nnj-=1
		nnj+=1
	gp = getparent(content,nj)
	#print "here"

#adding sibling leaves (the leftover nodes) and their properties 
#actually adding offsprings of the J 
while nj < len(content) and "#" not in content[nj]:
	# wrd = getword(content[nj])
	wrd = content[nj][content[nj].find(' '):] #extracting answer="x21 / word" from str="	:ARG1 (x21 / word"
	flag = False
	for x in nlist:
		if wrd in x:
			flag = True
			break
	if flag == False and nj!=j:
		wrd2 = getparent(content,nj)
		wrd2n = wrd2[1] 
		wrd2 = wrd2[0]
		# wrd2 = wrd2t[wrd2t.find(' '):]
		if wrd2n == j:
			wrd2 = getword(content[j]) #torture 
		# print ("##"+wrd2)
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
nlist[len(nlist)-1] = nlist[len(nlist)-1] + ")"*(br+1) 

#adding the ::snt and ::tok
tl = []
tl.append(content[tj-2])
tl.append(content[tj-1]+content[ti-1][7:])
tl.append(content[tj] + content[ti][7:])

nlist = tl + nlist
for x in nlist:
	print x


