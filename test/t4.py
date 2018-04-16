import re

str1 = [":ARG1-of (xap0 / base-01",":location (x20 / city",":ARG0 x2",":op6 and",":example-of (x21",":ARG0 (op21 / xerox"]
p = ".*x[0-9s].*"
for x in str1:
	print x
	if re.match(p,x):
		print("Found")
	else:
		print "None" 