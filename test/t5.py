import glob
import os
import subprocess

# /home/ritwik/ATS/dataset/cnn/stories


file = open("files.txt","r")
fileList = file.readlines()
file.close()

file = open("/home/ritwik/ATS/article.txt","w")
str2 = fileList[0].strip()
str1 = "/home/ritwik/ATS/dataset/dailymail/stories/" + str2
f2ile = open(str1,"r")
content = f2ile.readlines()

for x in content:
	file.write(x)

file.close()
f2ile.close()

file = open("/home/ritwik/ATS/currfile.txt","w")
file.write(str2)
file.close()

file = open("files.txt","w")
fileList = fileList[1:]
for x in fileList:
	file.write(x)
file.close()

# cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/cnn/stories/*'))
# file = open("files.txt","w")
# for x in cnnfiles:
# 	file.write(x[37:]+"\n")
# file.close()

# i=0
# for i in range(1,10):
# 	print cnnfiles[i][37:]

# subprocess.Popen("ls")

# print len(cnnfiles)