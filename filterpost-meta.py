import sys

infile = open(sys.argv[1],'r')
outfile = open(sys.argv[1]+'.new', 'w')

for l in infile:
	if l[0:9] == ".. tags: ":
		tags = set([item.strip().lower() for item in l[9:].split(",")])
		outfile.write(".. tags: {0}\n".format(",".join(list(tags))))
	else:
		outfile.write(l)

infile.close()
outfile.close()
