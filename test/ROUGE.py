# -*- coding: utf-8 -*-
import unicodedata
import glob
import json
from pyrouge import Rouge155
from pprint import pprint
from rouge import Rouge


# # # ROUGE155 from cnn_articles and cnn_toks
# print("ROUGE155 from dml_articles vs dml_toks")
# cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/dml_toks/*.story'))
# ck = len(cnnfiles)
# # ck = 10
# jsondata = '{"rouge_1_f_score": 0.0,"rouge_1_f_score_cb": 0.0,"rouge_1_f_score_ce": 0.0,"rouge_1_precision": 0.0,"rouge_1_precision_cb": 0.0,"rouge_1_precision_ce": 0.0,"rouge_1_recall": 0.0,"rouge_1_recall_cb": 0.0,"rouge_1_recall_ce": 0.0,"rouge_2_f_score": 0.0,"rouge_2_f_score_cb": 0.0,"rouge_2_f_score_ce": 0.0,"rouge_2_precision": 0.0,"rouge_2_precision_cb": 0.0,"rouge_2_precision_ce": 0.0,"rouge_2_recall": 0.0,"rouge_2_recall_cb": 0.0,"rouge_2_recall_ce": 0.0,"rouge_3_f_score": 0.0,"rouge_3_f_score_cb": 0.0,"rouge_3_f_score_ce": 0.0,"rouge_3_precision": 0.0,"rouge_3_precision_cb": 0.0,"rouge_3_precision_ce": 0.0,"rouge_3_recall": 0.0,"rouge_3_recall_cb": 0.0,"rouge_3_recall_ce": 0.0,"rouge_4_f_score": 0.0,"rouge_4_f_score_cb": 0.0,"rouge_4_f_score_ce": 0.0,"rouge_4_precision": 0.0,"rouge_4_precision_cb": 0.0,"rouge_4_precision_ce": 0.0,"rouge_4_recall": 0.0,"rouge_4_recall_cb": 0.0,"rouge_4_recall_ce": 0.0,"rouge_su4_f_score": 0.0,"rouge_su4_f_score_cb": 0.0,"rouge_su4_f_score_ce": 0.0,"rouge_su4_precision": 0.0,"rouge_su4_precision_cb": 0.0,"rouge_su4_precision_ce": 0.0,"rouge_su4_recall": 0.0,"rouge_su4_recall_cb": 0.0,"rouge_su4_recall_ce": 0.0}'
# jsonvals = json.loads(jsondata)
# # print jsonvals
# rouge = Rouge155(n_words=1000)
# k=0
# while k<len(cnnfiles):
# 	str1 = cnnfiles[k]  #[33:]
# 	file = open(str1,"r")
# 	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	str1 = "/home/ritwik/ATS/dataset/dml_articles/"+str1[34:]
# 	# str1 = "/home/ritwik/ATS/dataset/cnn_toks/"+str1[33:] #CNN_TOKS
# 	file = open(str1,"r")
# 	ref = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	str1 = ""
# 	for x in hypo:
# 		str1 = str1 + x + " "
# 	hypo = str1
# 	str1 = ""
# 	for x in ref:
# 		str1 = str1 + x + " "
# 	ref = str1.decode('ascii', 'ignore')
# 	str1 = ""
# 	ref_texts = {'A':ref}
# 	summary_text = hypo
# 	try:
# 		score = rouge.score_summary(summary_text, ref_texts)
# 	except:
# 		ck-=1
# 		print "Error at ", k+1
# 		k+=1
# 		continue

# 	for x in jsonvals.keys():
# 		jsonvals[x]+=score[x]
# 	k+=1
# 	print str(k)+"/"+str(ck)
# 	# if k==10:
# 	# 	break
# print "\n\n"

# for x in jsonvals.keys():
# 	jsonvals[x]/=ck

# file = open("/home/ritwik/ATS/dataset/RougeResults2.txt","a")
# file.write("ROUGE155 dml_articles vs dml_toks\n")
# for x in sorted(jsonvals.keys()):
# 	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
# file.write(str(ck))
# file.write("\n\n")
# file.close()

# # Dailymail
# print("ROUGE155 from dml_articles")
# cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))
# ck = len(cnnfiles)
# # ck = 10
# jsondata = '{"rouge_1_f_score": 0.0,"rouge_1_f_score_cb": 0.0,"rouge_1_f_score_ce": 0.0,"rouge_1_precision": 0.0,"rouge_1_precision_cb": 0.0,"rouge_1_precision_ce": 0.0,"rouge_1_recall": 0.0,"rouge_1_recall_cb": 0.0,"rouge_1_recall_ce": 0.0,"rouge_2_f_score": 0.0,"rouge_2_f_score_cb": 0.0,"rouge_2_f_score_ce": 0.0,"rouge_2_precision": 0.0,"rouge_2_precision_cb": 0.0,"rouge_2_precision_ce": 0.0,"rouge_2_recall": 0.0,"rouge_2_recall_cb": 0.0,"rouge_2_recall_ce": 0.0,"rouge_3_f_score": 0.0,"rouge_3_f_score_cb": 0.0,"rouge_3_f_score_ce": 0.0,"rouge_3_precision": 0.0,"rouge_3_precision_cb": 0.0,"rouge_3_precision_ce": 0.0,"rouge_3_recall": 0.0,"rouge_3_recall_cb": 0.0,"rouge_3_recall_ce": 0.0,"rouge_4_f_score": 0.0,"rouge_4_f_score_cb": 0.0,"rouge_4_f_score_ce": 0.0,"rouge_4_precision": 0.0,"rouge_4_precision_cb": 0.0,"rouge_4_precision_ce": 0.0,"rouge_4_recall": 0.0,"rouge_4_recall_cb": 0.0,"rouge_4_recall_ce": 0.0,"rouge_su4_f_score": 0.0,"rouge_su4_f_score_cb": 0.0,"rouge_su4_f_score_ce": 0.0,"rouge_su4_precision": 0.0,"rouge_su4_precision_cb": 0.0,"rouge_su4_precision_ce": 0.0,"rouge_su4_recall": 0.0,"rouge_su4_recall_cb": 0.0,"rouge_su4_recall_ce": 0.0}'
# jsonvals = json.loads(jsondata)
# # print jsonvals
# rouge = Rouge155(n_words=1000)
# k=0
# while k<len(cnnfiles):
# 	str1 = cnnfiles[k]
# 	file = open(str1,"r")
# 	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	str1 = "/home/ritwik/ATS/dataset/dml_articles/"+str1[34:]
# 	# str1 = "/home/ritwik/ATS/dataset/cnn_toks/"+str1[33:] #CNN_TOKS
# 	file = open(str1,"r")
# 	ref = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	str1 = ""
# 	for x in hypo:
# 		str1 = str1 + x + " "
# 	hypo = str1
# 	str1 = ""
# 	for x in ref:
# 		str1 = str1 + x + " "
# 	ref = str1.decode('ascii', 'ignore')
# 	str1 = ""
# 	ref_texts = {'A':ref}
# 	summary_text = hypo
# 	try:
# 		score = rouge.score_summary(summary_text, ref_texts)
# 	except:
# 		ck-=1
# 		print "Error at ", k+1
# 		k+=1
# 		continue

# 	for x in jsonvals.keys():
# 		jsonvals[x]+=score[x]
# 	k+=1
# 	print str(k)+"/"+str(ck)
# 	# if k==10:
# 	# 	break
# print "\n\n"

# for x in jsonvals.keys():
# 	jsonvals[x]/=ck

# file = open("/home/ritwik/ATS/dataset/RougeResults2.txt","a")
# file.write("ROUGE155 dml_articles vs mysummary\n")
# for x in sorted(jsonvals.keys()):
# 	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
# file.write(str(ck))
# file.write("\n\n")
# file.close()

# # # ROUGE155 from cnn_articles and cnn_toks
# print "ROUGE155 from dml_toks"
# cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))
# ck = len(cnnfiles)
# # ck = 10
# jsondata = '{"rouge_1_f_score": 0.0,"rouge_1_f_score_cb": 0.0,"rouge_1_f_score_ce": 0.0,"rouge_1_precision": 0.0,"rouge_1_precision_cb": 0.0,"rouge_1_precision_ce": 0.0,"rouge_1_recall": 0.0,"rouge_1_recall_cb": 0.0,"rouge_1_recall_ce": 0.0,"rouge_2_f_score": 0.0,"rouge_2_f_score_cb": 0.0,"rouge_2_f_score_ce": 0.0,"rouge_2_precision": 0.0,"rouge_2_precision_cb": 0.0,"rouge_2_precision_ce": 0.0,"rouge_2_recall": 0.0,"rouge_2_recall_cb": 0.0,"rouge_2_recall_ce": 0.0,"rouge_3_f_score": 0.0,"rouge_3_f_score_cb": 0.0,"rouge_3_f_score_ce": 0.0,"rouge_3_precision": 0.0,"rouge_3_precision_cb": 0.0,"rouge_3_precision_ce": 0.0,"rouge_3_recall": 0.0,"rouge_3_recall_cb": 0.0,"rouge_3_recall_ce": 0.0,"rouge_4_f_score": 0.0,"rouge_4_f_score_cb": 0.0,"rouge_4_f_score_ce": 0.0,"rouge_4_precision": 0.0,"rouge_4_precision_cb": 0.0,"rouge_4_precision_ce": 0.0,"rouge_4_recall": 0.0,"rouge_4_recall_cb": 0.0,"rouge_4_recall_ce": 0.0,"rouge_su4_f_score": 0.0,"rouge_su4_f_score_cb": 0.0,"rouge_su4_f_score_ce": 0.0,"rouge_su4_precision": 0.0,"rouge_su4_precision_cb": 0.0,"rouge_su4_precision_ce": 0.0,"rouge_su4_recall": 0.0,"rouge_su4_recall_cb": 0.0,"rouge_su4_recall_ce": 0.0}'
# jsonvals = json.loads(jsondata)
# # print jsonvals
# rouge = Rouge155(n_words=1000)
# k=0
# while k<len(cnnfiles):
# 	str1 = cnnfiles[k]  #[33:]
# 	file = open(str1,"r")
# 	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	# str1 = "/home/ritwik/ATS/dataset/cnn_articles/"+str1[33:]
# 	str1 = "/home/ritwik/ATS/dataset/dml_toks/"+str1[34:] #CNN_TOKS
# 	file = open(str1,"r")
# 	ref = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	str1 = ""
# 	for x in hypo:
# 		str1 = str1 + x + " "
# 	hypo = str1
# 	str1 = ""
# 	for x in ref:
# 		str1 = str1 + x + " "
# 	ref = str1.decode('ascii', 'ignore')
# 	str1 = ""
# 	ref_texts = {'A':ref}
# 	summary_text = hypo
# 	try:
# 		score = rouge.score_summary(summary_text, ref_texts)
# 	except:
# 		ck-=1
# 		print "Error at ", k+1
# 		k+=1
# 		continue
# 	for x in jsonvals.keys():
# 		jsonvals[x]+=score[x]
# 	k+=1
# 	print str(k)+"/"+str(ck)
# 	# if k==10:
# 	# 	break
# pprint(jsonvals)
# print "\n\n"
# for x in sorted(jsonvals.keys()):
# 	jsonvals[x]/=ck

# file = open("/home/ritwik/ATS/dataset/RougeResults2.txt","a")
# file.write("ROUGE155 dml_toks vs mysummary\n")
# for x in sorted(jsonvals.keys()):
# 	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
# file.write(str(ck))
# file.write("\n\n")
# file.close()


# # ROUGE SCORE FROM CNN_TOKS
# print "ROUGE SCORE FROM DML_TOKS"
# cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))
# ck = len(cnnfiles)
# rouge = Rouge()

# jsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
# jsonvals = json.loads(jsondata)
# artjsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
# artjsonvals = json.loads(artjsondata)
# print jsonvals
# k=0
# while k<len(cnnfiles):
# 	str1 = cnnfiles[k]  #[33:]
# 	file = open(str1,"r")
# 	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()
# 	str1 = "/home/ritwik/ATS/dataset/dml_toks/"+str1[34:]
# 	file = open(str1,"r")
# 	ref = [ x.strip().decode('ascii', 'ignore') for x in file.readlines() if x.strip() ]
# 	file.close()
# 	try:
# 		scores = rouge.get_scores(hypo, ref)
# 	except:
# 		ck-=1
# 		print "Error at ",k+1
# 		k+=1
# 		continue
# 	for x in scores:
# 		artjsonvals["rouge-1"]["f"] += x["rouge-1"]["f"]
# 		artjsonvals["rouge-1"]["p"] += x["rouge-1"]["p"]
# 		artjsonvals["rouge-1"]["r"] += x["rouge-1"]["r"]

# 		artjsonvals["rouge-2"]["f"] += x["rouge-2"]["f"]
# 		artjsonvals["rouge-2"]["p"] += x["rouge-2"]["p"]
# 		artjsonvals["rouge-2"]["r"] += x["rouge-2"]["r"]

# 		artjsonvals["rouge-l"]["f"] += x["rouge-l"]["f"]
# 		artjsonvals["rouge-l"]["p"] += x["rouge-l"]["p"]
# 		artjsonvals["rouge-l"]["r"] += x["rouge-l"]["r"]

# 	ck2 = len(scores)
# 	if ck2 == 0:
# 		ck-=1
# 		print "Division Error at ",k+1
# 		k+=1
# 		continue
# 	artjsonvals["rouge-1"]["f"] /= ck2
# 	artjsonvals["rouge-1"]["p"] /= ck2
# 	artjsonvals["rouge-1"]["r"] /= ck2

# 	artjsonvals["rouge-2"]["f"] /= ck2
# 	artjsonvals["rouge-2"]["p"] /= ck2
# 	artjsonvals["rouge-2"]["r"] /= ck2

# 	artjsonvals["rouge-l"]["f"] /= ck2
# 	artjsonvals["rouge-l"]["p"] /= ck2
# 	artjsonvals["rouge-l"]["r"] /= ck2

# 	jsonvals["rouge-1"]["f"] += artjsonvals["rouge-1"]["f"]
# 	jsonvals["rouge-1"]["p"] += artjsonvals["rouge-1"]["p"]
# 	jsonvals["rouge-1"]["r"] += artjsonvals["rouge-1"]["r"]

# 	jsonvals["rouge-2"]["f"] += artjsonvals["rouge-2"]["f"]
# 	jsonvals["rouge-2"]["p"] += artjsonvals["rouge-2"]["p"]
# 	jsonvals["rouge-2"]["r"] += artjsonvals["rouge-2"]["r"]

# 	jsonvals["rouge-l"]["f"] += artjsonvals["rouge-l"]["f"]
# 	jsonvals["rouge-l"]["p"] += artjsonvals["rouge-l"]["p"]
# 	jsonvals["rouge-l"]["r"] += artjsonvals["rouge-l"]["r"]
# 	k+=1
# 	print str(k)+"/"+str(ck)

# # print jsonvals
# jsonvals["rouge-1"]["f"] /= ck
# jsonvals["rouge-1"]["p"] /= ck
# jsonvals["rouge-1"]["r"] /= ck

# jsonvals["rouge-2"]["f"] /= ck
# jsonvals["rouge-2"]["p"] /= ck
# jsonvals["rouge-2"]["r"] /= ck

# jsonvals["rouge-l"]["f"] /= ck
# jsonvals["rouge-l"]["p"] /= ck
# jsonvals["rouge-l"]["r"] /= ck
# # print jsonvals
# file = open("/home/ritwik/ATS/dataset/RougeResults2.txt","a")
# file.write("Rouge dml_toks vs mysummary\n")
# for x in sorted(jsonvals.keys()):
# 	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
# file.write(str(ck))
# file.write("\n\n")
# file.close()




# ROUGE SCORE FROM CNN_ARTICLES
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))
ck = len(cnnfiles)
rouge = Rouge()
print "ROUGE SCORE FROM DML_ARTICLES"
jsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
jsonvals = json.loads(jsondata)
print jsonvals
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/dml_articles/"+str1[34:]
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	try:
		scores = rouge.get_scores(hypo, ref)
	except:
		ck-=1
		print "Error in",k+1
		k+=1
		continue
	jsonvals["rouge-1"]["f"] += scores[0]["rouge-1"]["f"]
	jsonvals["rouge-1"]["p"] += scores[0]["rouge-1"]["p"]
	jsonvals["rouge-1"]["r"] += scores[0]["rouge-1"]["r"]

	jsonvals["rouge-2"]["f"] += scores[0]["rouge-2"]["f"]
	jsonvals["rouge-2"]["p"] += scores[0]["rouge-2"]["p"]
	jsonvals["rouge-2"]["r"] += scores[0]["rouge-2"]["r"]

	jsonvals["rouge-l"]["f"] += scores[0]["rouge-l"]["f"]
	jsonvals["rouge-l"]["p"] += scores[0]["rouge-l"]["p"]
	jsonvals["rouge-l"]["r"] += scores[0]["rouge-l"]["r"]
	k+=1
	print str(k)+"/"+str(ck)
 
print jsonvals, "\n\n"
jsonvals["rouge-1"]["f"] /= ck
jsonvals["rouge-1"]["p"] /= ck
jsonvals["rouge-1"]["r"] /= ck

jsonvals["rouge-2"]["f"] /= ck
jsonvals["rouge-2"]["p"] /= ck
jsonvals["rouge-2"]["r"] /= ck

jsonvals["rouge-l"]["f"] /= ck
jsonvals["rouge-l"]["p"] /= ck
jsonvals["rouge-l"]["r"] /= ck
print jsonvals
file = open("/home/ritwik/ATS/dataset/RougeResults2.txt","a")
file.write("Rouge dml_articles vs mysummary\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()


# ROUGE SCORE FROM CNN_ARTICLES vs cnn_toks
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/dml_toks/*.story'))
ck = len(cnnfiles)
rouge = Rouge()
print "ROUGE SCORE FROM DML_ARTICLES vs dml_toks"
jsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
jsonvals = json.loads(jsondata)
print jsonvals
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/dml_articles/"+str1[34:]
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	try:
		scores = rouge.get_scores(hypo, ref)
	except:
		ck-=1
		print "Error in",k+1
		k+=1
		continue
	jsonvals["rouge-1"]["f"] += scores[0]["rouge-1"]["f"]
	jsonvals["rouge-1"]["p"] += scores[0]["rouge-1"]["p"]
	jsonvals["rouge-1"]["r"] += scores[0]["rouge-1"]["r"]

	jsonvals["rouge-2"]["f"] += scores[0]["rouge-2"]["f"]
	jsonvals["rouge-2"]["p"] += scores[0]["rouge-2"]["p"]
	jsonvals["rouge-2"]["r"] += scores[0]["rouge-2"]["r"]

	jsonvals["rouge-l"]["f"] += scores[0]["rouge-l"]["f"]
	jsonvals["rouge-l"]["p"] += scores[0]["rouge-l"]["p"]
	jsonvals["rouge-l"]["r"] += scores[0]["rouge-l"]["r"]
	k+=1
	print str(k)+"/"+str(ck)
 
print jsonvals, "\n\n"
jsonvals["rouge-1"]["f"] /= ck
jsonvals["rouge-1"]["p"] /= ck
jsonvals["rouge-1"]["r"] /= ck

jsonvals["rouge-2"]["f"] /= ck
jsonvals["rouge-2"]["p"] /= ck
jsonvals["rouge-2"]["r"] /= ck

jsonvals["rouge-l"]["f"] /= ck
jsonvals["rouge-l"]["p"] /= ck
jsonvals["rouge-l"]["r"] /= ck
print jsonvals
file = open("/home/ritwik/ATS/dataset/RougeResults2.txt","a")
file.write("Rouge dml_articles vs dml_toks\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()


# # ROUGE155 from cnn_articles and cnn_toks
print("ROUGE155 from cnn_articles vs cnn_toks")
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/cnn_toks/*.story'))
ck = len(cnnfiles)
# ck = 10
jsondata = '{"rouge_1_f_score": 0.0,"rouge_1_f_score_cb": 0.0,"rouge_1_f_score_ce": 0.0,"rouge_1_precision": 0.0,"rouge_1_precision_cb": 0.0,"rouge_1_precision_ce": 0.0,"rouge_1_recall": 0.0,"rouge_1_recall_cb": 0.0,"rouge_1_recall_ce": 0.0,"rouge_2_f_score": 0.0,"rouge_2_f_score_cb": 0.0,"rouge_2_f_score_ce": 0.0,"rouge_2_precision": 0.0,"rouge_2_precision_cb": 0.0,"rouge_2_precision_ce": 0.0,"rouge_2_recall": 0.0,"rouge_2_recall_cb": 0.0,"rouge_2_recall_ce": 0.0,"rouge_3_f_score": 0.0,"rouge_3_f_score_cb": 0.0,"rouge_3_f_score_ce": 0.0,"rouge_3_precision": 0.0,"rouge_3_precision_cb": 0.0,"rouge_3_precision_ce": 0.0,"rouge_3_recall": 0.0,"rouge_3_recall_cb": 0.0,"rouge_3_recall_ce": 0.0,"rouge_4_f_score": 0.0,"rouge_4_f_score_cb": 0.0,"rouge_4_f_score_ce": 0.0,"rouge_4_precision": 0.0,"rouge_4_precision_cb": 0.0,"rouge_4_precision_ce": 0.0,"rouge_4_recall": 0.0,"rouge_4_recall_cb": 0.0,"rouge_4_recall_ce": 0.0,"rouge_su4_f_score": 0.0,"rouge_su4_f_score_cb": 0.0,"rouge_su4_f_score_ce": 0.0,"rouge_su4_precision": 0.0,"rouge_su4_precision_cb": 0.0,"rouge_su4_precision_ce": 0.0,"rouge_su4_recall": 0.0,"rouge_su4_recall_cb": 0.0,"rouge_su4_recall_ce": 0.0}'
jsonvals = json.loads(jsondata)
# print jsonvals
rouge = Rouge155(n_words=1000)
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/cnn_articles/"+str1[34:]
	# str1 = "/home/ritwik/ATS/dataset/cnn_toks/"+str1[33:] #CNN_TOKS
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	ref_texts = {'A':ref}
	summary_text = hypo
	try:
		score = rouge.score_summary(summary_text, ref_texts)
	except:
		ck-=1
		print "Error at ", k+1
		k+=1
		continue

	for x in jsonvals.keys():
		jsonvals[x]+=score[x]
	k+=1
	print str(k)+"/"+str(ck)
	# if k==10:
	# 	break
print "\n\n"

for x in jsonvals.keys():
	jsonvals[x]/=ck

file = open("/home/ritwik/ATS/dataset/RougeResults.txt","a")
file.write("ROUGE155 cnn_articles vs cnn_toks\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()


# # ROUGE155 from cnn_articles and cnn_toks
print("ROUGE155 from cnn_articles")
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results/*.story'))
ck = len(cnnfiles)
# ck = 10
jsondata = '{"rouge_1_f_score": 0.0,"rouge_1_f_score_cb": 0.0,"rouge_1_f_score_ce": 0.0,"rouge_1_precision": 0.0,"rouge_1_precision_cb": 0.0,"rouge_1_precision_ce": 0.0,"rouge_1_recall": 0.0,"rouge_1_recall_cb": 0.0,"rouge_1_recall_ce": 0.0,"rouge_2_f_score": 0.0,"rouge_2_f_score_cb": 0.0,"rouge_2_f_score_ce": 0.0,"rouge_2_precision": 0.0,"rouge_2_precision_cb": 0.0,"rouge_2_precision_ce": 0.0,"rouge_2_recall": 0.0,"rouge_2_recall_cb": 0.0,"rouge_2_recall_ce": 0.0,"rouge_3_f_score": 0.0,"rouge_3_f_score_cb": 0.0,"rouge_3_f_score_ce": 0.0,"rouge_3_precision": 0.0,"rouge_3_precision_cb": 0.0,"rouge_3_precision_ce": 0.0,"rouge_3_recall": 0.0,"rouge_3_recall_cb": 0.0,"rouge_3_recall_ce": 0.0,"rouge_4_f_score": 0.0,"rouge_4_f_score_cb": 0.0,"rouge_4_f_score_ce": 0.0,"rouge_4_precision": 0.0,"rouge_4_precision_cb": 0.0,"rouge_4_precision_ce": 0.0,"rouge_4_recall": 0.0,"rouge_4_recall_cb": 0.0,"rouge_4_recall_ce": 0.0,"rouge_su4_f_score": 0.0,"rouge_su4_f_score_cb": 0.0,"rouge_su4_f_score_ce": 0.0,"rouge_su4_precision": 0.0,"rouge_su4_precision_cb": 0.0,"rouge_su4_precision_ce": 0.0,"rouge_su4_recall": 0.0,"rouge_su4_recall_cb": 0.0,"rouge_su4_recall_ce": 0.0}'
jsonvals = json.loads(jsondata)
# print jsonvals
rouge = Rouge155(n_words=1000)
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/cnn_articles/"+str1[33:]
	# str1 = "/home/ritwik/ATS/dataset/cnn_toks/"+str1[33:] #CNN_TOKS
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	ref_texts = {'A':ref}
	summary_text = hypo
	try:
		score = rouge.score_summary(summary_text, ref_texts)
	except:
		ck-=1
		print "Error at ", k+1
		k+=1
		continue

	for x in jsonvals.keys():
		jsonvals[x]+=score[x]
	k+=1
	print str(k)+"/"+str(ck)
	# if k==10:
	# 	break
print "\n\n"

for x in jsonvals.keys():
	jsonvals[x]/=ck

file = open("/home/ritwik/ATS/dataset/RougeResults.txt","a")
file.write("ROUGE155 cnn_articles vs mysummary\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()

# ROUGE155 from cnn_articles and cnn_toks
print "ROUGE155 from cnn_toks"
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results/*.story'))
ck = len(cnnfiles)
# ck = 10
jsondata = '{"rouge_1_f_score": 0.0,"rouge_1_f_score_cb": 0.0,"rouge_1_f_score_ce": 0.0,"rouge_1_precision": 0.0,"rouge_1_precision_cb": 0.0,"rouge_1_precision_ce": 0.0,"rouge_1_recall": 0.0,"rouge_1_recall_cb": 0.0,"rouge_1_recall_ce": 0.0,"rouge_2_f_score": 0.0,"rouge_2_f_score_cb": 0.0,"rouge_2_f_score_ce": 0.0,"rouge_2_precision": 0.0,"rouge_2_precision_cb": 0.0,"rouge_2_precision_ce": 0.0,"rouge_2_recall": 0.0,"rouge_2_recall_cb": 0.0,"rouge_2_recall_ce": 0.0,"rouge_3_f_score": 0.0,"rouge_3_f_score_cb": 0.0,"rouge_3_f_score_ce": 0.0,"rouge_3_precision": 0.0,"rouge_3_precision_cb": 0.0,"rouge_3_precision_ce": 0.0,"rouge_3_recall": 0.0,"rouge_3_recall_cb": 0.0,"rouge_3_recall_ce": 0.0,"rouge_4_f_score": 0.0,"rouge_4_f_score_cb": 0.0,"rouge_4_f_score_ce": 0.0,"rouge_4_precision": 0.0,"rouge_4_precision_cb": 0.0,"rouge_4_precision_ce": 0.0,"rouge_4_recall": 0.0,"rouge_4_recall_cb": 0.0,"rouge_4_recall_ce": 0.0,"rouge_su4_f_score": 0.0,"rouge_su4_f_score_cb": 0.0,"rouge_su4_f_score_ce": 0.0,"rouge_su4_precision": 0.0,"rouge_su4_precision_cb": 0.0,"rouge_su4_precision_ce": 0.0,"rouge_su4_recall": 0.0,"rouge_su4_recall_cb": 0.0,"rouge_su4_recall_ce": 0.0}'
jsonvals = json.loads(jsondata)
# print jsonvals
rouge = Rouge155(n_words=1000)
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	# str1 = "/home/ritwik/ATS/dataset/cnn_articles/"+str1[33:]
	str1 = "/home/ritwik/ATS/dataset/cnn_toks/"+str1[33:] #CNN_TOKS
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	ref_texts = {'A':ref}
	summary_text = hypo
	try:
		score = rouge.score_summary(summary_text, ref_texts)
	except:
		ck-=1
		print "Error at ", k+1
		k+=1
		continue
	for x in jsonvals.keys():
		jsonvals[x]+=score[x]
	k+=1
	print str(k)+"/"+str(ck)
	# if k==10:
	# 	break
pprint(jsonvals)
print "\n\n"
for x in sorted(jsonvals.keys()):
	jsonvals[x]/=ck

file = open("/home/ritwik/ATS/dataset/RougeResults.txt","a")
file.write("ROUGE155 cnn_toks vs mysummary\n")
for x in jsonvals.keys():
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()


# ROUGE SCORE FROM CNN_TOKS
print "ROUGE SCORE FROM CNN_TOKS"
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results/*.story'))
ck = len(cnnfiles)
rouge = Rouge()

jsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
jsonvals = json.loads(jsondata)
artjsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
artjsonvals = json.loads(artjsondata)
print jsonvals
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/cnn_toks/"+str1[33:]
	file = open(str1,"r")
	ref = [ x.strip().decode('ascii', 'ignore') for x in file.readlines() if x.strip() ]
	file.close()
	try:
		scores = rouge.get_scores(hypo, ref)
	except:
		ck-=1
		print "Error at ",k+1
		k+=1
		continue
	for x in scores:
		artjsonvals["rouge-1"]["f"] += x["rouge-1"]["f"]
		artjsonvals["rouge-1"]["p"] += x["rouge-1"]["p"]
		artjsonvals["rouge-1"]["r"] += x["rouge-1"]["r"]

		artjsonvals["rouge-2"]["f"] += x["rouge-2"]["f"]
		artjsonvals["rouge-2"]["p"] += x["rouge-2"]["p"]
		artjsonvals["rouge-2"]["r"] += x["rouge-2"]["r"]

		artjsonvals["rouge-l"]["f"] += x["rouge-l"]["f"]
		artjsonvals["rouge-l"]["p"] += x["rouge-l"]["p"]
		artjsonvals["rouge-l"]["r"] += x["rouge-l"]["r"]

	ck2 = len(scores)
	if ck2 == 0:
		ck-=1
		print "Division Error at ",k+1
		k+=1
		continue
	artjsonvals["rouge-1"]["f"] /= ck2
	artjsonvals["rouge-1"]["p"] /= ck2
	artjsonvals["rouge-1"]["r"] /= ck2

	artjsonvals["rouge-2"]["f"] /= ck2
	artjsonvals["rouge-2"]["p"] /= ck2
	artjsonvals["rouge-2"]["r"] /= ck2

	artjsonvals["rouge-l"]["f"] /= ck2
	artjsonvals["rouge-l"]["p"] /= ck2
	artjsonvals["rouge-l"]["r"] /= ck2

	jsonvals["rouge-1"]["f"] += artjsonvals["rouge-1"]["f"]
	jsonvals["rouge-1"]["p"] += artjsonvals["rouge-1"]["p"]
	jsonvals["rouge-1"]["r"] += artjsonvals["rouge-1"]["r"]

	jsonvals["rouge-2"]["f"] += artjsonvals["rouge-2"]["f"]
	jsonvals["rouge-2"]["p"] += artjsonvals["rouge-2"]["p"]
	jsonvals["rouge-2"]["r"] += artjsonvals["rouge-2"]["r"]

	jsonvals["rouge-l"]["f"] += artjsonvals["rouge-l"]["f"]
	jsonvals["rouge-l"]["p"] += artjsonvals["rouge-l"]["p"]
	jsonvals["rouge-l"]["r"] += artjsonvals["rouge-l"]["r"]
	k+=1
	print str(k)+"/"+str(ck)

# print jsonvals
jsonvals["rouge-1"]["f"] /= ck
jsonvals["rouge-1"]["p"] /= ck
jsonvals["rouge-1"]["r"] /= ck

jsonvals["rouge-2"]["f"] /= ck
jsonvals["rouge-2"]["p"] /= ck
jsonvals["rouge-2"]["r"] /= ck

jsonvals["rouge-l"]["f"] /= ck
jsonvals["rouge-l"]["p"] /= ck
jsonvals["rouge-l"]["r"] /= ck
# print jsonvals
file = open("/home/ritwik/ATS/dataset/RougeResults.txt","a")
file.write("Rouge cnn_toks vs mysummary\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()




# ROUGE SCORE FROM CNN_ARTICLES
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/results/*.story'))
ck = len(cnnfiles)
rouge = Rouge()
print "ROUGE SCORE FROM CNN_ARTICLES"
jsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
jsonvals = json.loads(jsondata)
print jsonvals
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/cnn_articles/"+str1[33:]
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	try:
		scores = rouge.get_scores(hypo, ref)
	except:
		ck-=1
		print "Error in",k+1
		k+=1
		continue
	jsonvals["rouge-1"]["f"] += scores[0]["rouge-1"]["f"]
	jsonvals["rouge-1"]["p"] += scores[0]["rouge-1"]["p"]
	jsonvals["rouge-1"]["r"] += scores[0]["rouge-1"]["r"]

	jsonvals["rouge-2"]["f"] += scores[0]["rouge-2"]["f"]
	jsonvals["rouge-2"]["p"] += scores[0]["rouge-2"]["p"]
	jsonvals["rouge-2"]["r"] += scores[0]["rouge-2"]["r"]

	jsonvals["rouge-l"]["f"] += scores[0]["rouge-l"]["f"]
	jsonvals["rouge-l"]["p"] += scores[0]["rouge-l"]["p"]
	jsonvals["rouge-l"]["r"] += scores[0]["rouge-l"]["r"]
	k+=1
	print str(k)+"/"+str(ck)
 
print jsonvals, "\n\n"
jsonvals["rouge-1"]["f"] /= ck
jsonvals["rouge-1"]["p"] /= ck
jsonvals["rouge-1"]["r"] /= ck

jsonvals["rouge-2"]["f"] /= ck
jsonvals["rouge-2"]["p"] /= ck
jsonvals["rouge-2"]["r"] /= ck

jsonvals["rouge-l"]["f"] /= ck
jsonvals["rouge-l"]["p"] /= ck
jsonvals["rouge-l"]["r"] /= ck
print jsonvals
file = open("/home/ritwik/ATS/dataset/RougeResults.txt","a")
file.write("Rouge cnn_articles vs mysummary\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()

# ROUGE SCORE FROM CNN_ARTICLES vs cnn_toks
cnnfiles = sorted(glob.glob('/home/ritwik/ATS/dataset/cnn_toks/*.story'))
ck = len(cnnfiles)
rouge = Rouge()
print "ROUGE SCORE FROM CNN_ARTICLES vs cnn_toks"
jsondata = '{"rouge-1": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-2": {"f": 0.0,"p": 0.0,"r": 0.0},"rouge-l": {"f": 0.0,"p": 0.0,"r": 0.0}}'
jsonvals = json.loads(jsondata)
print jsonvals
k=0
while k<len(cnnfiles):
	str1 = cnnfiles[k]  #[33:]
	file = open(str1,"r")
	hypo = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = "/home/ritwik/ATS/dataset/cnn_articles/"+str1[34:]
	file = open(str1,"r")
	ref = [ x.strip() for x in file.readlines() if x.strip() ]
	file.close()
	str1 = ""
	for x in hypo:
		str1 = str1 + x + " "
	hypo = str1
	str1 = ""
	for x in ref:
		str1 = str1 + x + " "
	ref = str1.decode('ascii', 'ignore')
	str1 = ""
	try:
		scores = rouge.get_scores(hypo, ref)
	except:
		ck-=1
		print "Error in",k+1
		k+=1
		continue
	jsonvals["rouge-1"]["f"] += scores[0]["rouge-1"]["f"]
	jsonvals["rouge-1"]["p"] += scores[0]["rouge-1"]["p"]
	jsonvals["rouge-1"]["r"] += scores[0]["rouge-1"]["r"]

	jsonvals["rouge-2"]["f"] += scores[0]["rouge-2"]["f"]
	jsonvals["rouge-2"]["p"] += scores[0]["rouge-2"]["p"]
	jsonvals["rouge-2"]["r"] += scores[0]["rouge-2"]["r"]

	jsonvals["rouge-l"]["f"] += scores[0]["rouge-l"]["f"]
	jsonvals["rouge-l"]["p"] += scores[0]["rouge-l"]["p"]
	jsonvals["rouge-l"]["r"] += scores[0]["rouge-l"]["r"]
	k+=1
	print str(k)+"/"+str(ck)
 
print jsonvals, "\n\n"
jsonvals["rouge-1"]["f"] /= ck
jsonvals["rouge-1"]["p"] /= ck
jsonvals["rouge-1"]["r"] /= ck

jsonvals["rouge-2"]["f"] /= ck
jsonvals["rouge-2"]["p"] /= ck
jsonvals["rouge-2"]["r"] /= ck

jsonvals["rouge-l"]["f"] /= ck
jsonvals["rouge-l"]["p"] /= ck
jsonvals["rouge-l"]["r"] /= ck
print jsonvals
file = open("/home/ritwik/ATS/dataset/RougeResults.txt","a")
file.write("Rouge cnn_articles vs cnn_toks\n")
for x in sorted(jsonvals.keys()):
	file.write("\t\t"+str(x)+": "+str(jsonvals[x])+"\n")
file.write(str(ck))
file.write("\n\n")
file.close()



# FOR EXTRACTING ONLY ARTICLES FROM GIVEN DATASET i.e. omiting "@highlight" everywhere
# file = open("files3.txt","r")
# fileList = [ x.strip() for x in file.readlines()]
# file.close()
# fileList = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))

# k=0
# while k<4718: #2058 for CNN and 4718 for Dailymail
# 	str1 = fileList[k][34:] #33 for CNN and 34 for Dailymail
# 	str1 = "/home/ritwik/ATS/dataset/dailymail/stories/" + str1
# 	f2ile = open(str1,"r")
# 	content = f2ile.readlines()
# 	f2ile.close()
# 	str1 = "/home/ritwik/ATS/dataset/dml_articles/"+fileList[k][33:]
# 	file = open(str1,"w")
# 	for x in content:
# 		if "@highlight" in x:
# 			break
# 		file.write(x)
# 	file.close()
# 	k+=1
# 	print str(k)+"/4718"


#FOR EXTRACTING ::tok from AMRs
# fileList = sorted(glob.glob('/home/ritwik/ATS/dataset/results2/*.story'))

# k=0
# while k<4718: #2058 for CNN and 4718 for Dailymail
# 	str1 = fileList[k][34:] #33 for CNN and 34 for Dailymail
# 	str1 = str1[:-6]+"SUMMED.story"
# 	str1 = "/home/ritwik/ATS/dataset/results2/AMRs/" + str1
# 	file = open(str1,"r")
# 	content = [ x.strip() for x in file.readlines() if x.strip() ]
# 	file.close()

# 	str1 = fileList[k][33:]
# 	str1 = "/home/ritwik/ATS/dataset/dml_toks/"+str1
# 	file = open(str1,"w")

# 	for x in content:
# 		if "# ::tok" in x:
# 			file.write(x[8:]+"\n")

# 	file.close()
# 	print str(k)+"/4718"

# 	k+=1