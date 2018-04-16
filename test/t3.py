# def gettabs (str1):
# 	ts = len(str1) - len(str1.lstrip('	'))
# 	return ts

# def gettag (str1):
# 	k = str1.find(':')
# 	l = str1.find('(')
# 	return str1[k+1:l-1]

# def getparent (content, j):
# 	k = gettabs(content[j])
# 	#print k
# 	if k==0:
# 		return ["END",-1]
# 	while "# ::" not in content[j-1]:
# 		if gettabs(content[j-1]) == k-1:
# 			kk = content[j-1].find('(')
# 			return [content[j-1][kk:],j-1]
# 		j=j-1

# def getword (str1):
# 	k = str1.find('/')
# 	return str1[k+1:]

# def graphMerge(content, i, j, windx1, windx2):
	
# 	ti=i
# 	tj=j
# 	# print ("i = "+str(i)+" j = "+str(j))
# 	str1 = "x"+str(windx2)+" "
# 	#print ("#### 15"+content[15])

# 	i+=1
# 	#find that word in below amr; stored in i 
# 	while str1 not in content[i]:
# 		if "# ::tok" in content[i] or i==len(content)-1:
# 			print ("ERROR!")
# 			exit()
# 		i+=1

# 	# print content[i]
# 	str1 = "x"+str(windx1)+" "

# 	j+=1
# 	#find that word in above amr
# 	while str1 not in content[j]:
# 		if "# ::tok" in content[j] or j==len(content)-1:
# 			print ("ERROR!")
# 			# print ("i = "+str(i)+" j = "+str(j))
# 			# print (str(windx2)+" "+str(windx1))
# 			# print content[i]
# 			exit()
# 		j+=1

# 	#print ("Index of the below line containing given word "+str(i))
# 	#print content[i] #below
# 	#print ("Index of the above line containing given word "+str(j))
# 	#print content[j] #above
# 	#print (len(content[tj].split())-2)

# 	#adding bias to the below tokens
# 	bias = len(content[tj].split())-2
# 	k=ti+1
# 	while k < len(content) and "#" not in content[k]:
# 		if k != i and 'x' in content[k]:
# 			kt = content[k].find('/')
# 			kp = content[k].find('(')
# 			if kt == -1 or kp ==-1:
# 				kq = content[k].find('x')
# 				nn = int(content[k][kq+1:].lstrip())
# 				kp = kq-1
# 				kt = len(content[k])+1
# 			else:
# 				#print content[k][kp+2:kt-1]
# 				nn = int(content[k][kp+2:kt-1])
# 			nn = nn + bias
# 			content[k] = content[k][:kp+2] + str(nn) + content[k][kt-1:]
# 		k+=1

# 	#getting parents and merging 
# 	nlist = []
# 	nlist.append(content[i])
# 	nj = j
# 	gp = getparent(content,nj)
# 	ts = gettabs(content[i])
# 	while gp[1] != -1:
# 		str1 = gettag(content[nj])+"-of "+gp[0]
# 		ts+=1
# 		str1 = "	" * ts + ":" + str1
# 		str1 = str1.replace('-of-of','')
# 		# print "#############"
# 		# print str1
# 		# print "#####"
# 		nlist.append(str1)
# 		# print gp
# 		nj = gp[1] #parent
# 		nnj = nj+1 #child
# 		nntb = gettabs (content[nj]) #tabs in parent
# 		while gettabs(content[nnj])>nntb:
# 			if gettabs(content[nnj]) == nntb + 1:
# 				# print ("Child is == "+content[nnj])
# 				flag = False
# 				for x in nlist:
# 					if getword(content[nnj]) in x:
# 						flag = True
# 						break
# 				if flag == False:
# 					str1 = "	"*(ts+1) + content[nnj].lstrip()
# 					nlist.append(str1)
# 					nnj+=1
# 					while gettabs(content[nnj])>nntb+1:
# 						str1 = "	" * (ts+1+(gettabs(content[nnj])-nntb-1)) + content[nnj].lstrip()
# 						nlist.append(str1)
# 						nnj+=1
# 					if gettabs(content[nnj])<=nntb+1:
# 						nnj-=1
# 			nnj+=1
# 		gp = getparent(content,nj)
# 		#print "here"

# 	#adding sibling leaves (the leftover nodes) and their properties 
# 	while nj < len(content) and "#" not in content[nj]:
# 		wrd = getword(content[nj])
# 		flag = False
# 		for x in nlist:
# 			if wrd in x:
# 				flag = True
# 				break
# 		if flag == False:
# 			wrd2 = getword(getparent(content,nj)[0])
# 			#print wrd2
# 			for x in nlist:
# 				if wrd2 in x:
# 					k = gettabs(x)
# 					str1 = "	" * (k+1) + content[nj].lstrip('	')
# 					#print str1
# 					nlist.append(str1)
# 		nj+=1

# 	ii=i
# 	if ti+1 == ii:
# 		ii+=1
# 	ti2 =ti
# 	while "# ::id" not in content[ti2]:
# 		ti2+=1
# 		if ti2 == len(content) -1:
# 			break
# 	#print ti2
# 	nlist = content[ti+1:ii]+nlist+content[i+1:ti2]

# 	#bracket balancing
# 	k = 0
# 	br = 0
# 	while k<len(nlist)-1:
# 		if "(" in nlist[k]:
# 			if gettabs(nlist[k+1]) <= gettabs(nlist[k]):
# 				nlist[k] = nlist[k] + ")"*(gettabs(nlist[k])-gettabs(nlist[k+1])+1)
# 				br = br - (gettabs(nlist[k])-gettabs(nlist[k+1]))
# 			else:
# 				br+=1
# 		else:
# 			if gettabs(nlist[k+1]) < gettabs(nlist[k]):
# 				nlist[k] = nlist[k] + ")"*(gettabs(nlist[k])-gettabs(nlist[k+1]))
# 				br = br - (gettabs(nlist[k])-gettabs(nlist[k+1]))
# 		k+=1
# 	nlist[len(nlist)-1] = nlist[len(nlist)-1] + ")"*(br+1) 

# 	#adding the ::snt and ::tok
# 	tl = []
# 	tl.append(content[tj-2])
# 	tl.append(content[tj-1]+content[ti-1][7:])
# 	tl.append(content[tj] + content[ti][7:])

# 	nlist = tl + nlist

# 	# for x in nlist:
# 	# 	print x

# 	return nlist
	

# def getCommonWord(str1, str2):
# 	# str1 = "Some scoff at the notion that movies do anything more than entertain ."
# 	# str2 = "Some are wrong ."
# 	ml1 = str1.split()
# 	ml2 = str2.split()

# 	ml3 = set(ml1).intersection(ml2)
# 	# print ml3
# 	file = open("stpwrds.txt", "r+")
# 	stpwrds=[x.rstrip('\n').rstrip(')') for x in file.readlines() if x.strip()]
# 	file.close()
# 	ml4 = set(ml3).difference(stpwrds)
# 	# print ml4
# 	return ml4

	

# file = open("art.txt","r+")
# file2 = open("summ.txt","w")
# #content=[x.rstrip() for x in file.readlines() if x.strip()]
# content=[x.rstrip('\n') for x in file.readlines() if x.strip()]
# content2 = []
# for x in content:
# 	content2.append(x.rstrip(')'))

# i=j=k=0

# while k<len(content):
# 	if "::tok" in content[k] and j==0 and i==0:
# 		j=k
# 	elif "::tok" in content[k] and j!=0 and i==0:
# 		i=k
# 	if i!=0 and j!=0:
# 		cw = getCommonWord(content[i], content[j])
# 		if len(cw) == 0:
# 			j=i
# 			i=0
# 			# print "Here"
# 		else:
# 			print cw
# 			ml = list(cw)
# 			windx1 = content[j].split().index(ml[0]) - 1
# 			windx2 = content[i].split().index(ml[0]) - 1
# 			# if ml[0]=="bin":
# 			# print (content[i])
# 			# print (content[j])
# 			#print ("i ="+str(i)+" j="+str(j))

# 			# print windx1
# 			# print windx2
# 			# print i
# 			# print j
# 			nlist = graphMerge(content2, i, j, windx1, windx2)
# 			ti2 = i
# 			while "# ::id" not in content[ti2]:
# 				ti2+=1
# 				if ti2 == len(content) -1:
# 					break
# 			content = content[:j-1] + nlist[1:] + content[ti2:]
# 			content2 = []
# 			for x in content:
# 				content2.append(x.rstrip(')'))
# 			# print "here"
# 			# print ""
# 			k=j-2
# 			i=j=0
			
# 	k+=1
# print "################################################"
# for x in content:
# 	if "# ::id" in x:
# 		file2.write("\n")
# 		print ""
# 	file2.write(x+"\n")
# 	print x
	

# file2.close()

# file.close()


import time
import threading
import sys
import random


# while True:
#     sys.stdout.write(".")
#     sys.stdout.flush()
#     time.sleep(1) # delays for 1 seconds

k=1
i=1001
while True:
	if i>random.randint(100,2000):
		# print ("Stage "+str(k))
		sys.stdout.write("\n"+"### Creating sentence level grammars ###"+"\n")
		sys.stdout.write("\n"+"Stage "+str(k)+"\n")
		sys.stdout.flush()
		k+=1
		i=0
	# for k in xrange(1,3):
	sys.stdout.write(".")
	sys.stdout.flush()
	time.sleep(1)
	# print ("")
	i+=1
