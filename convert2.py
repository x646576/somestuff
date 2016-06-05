import re
def convert(col):
	def opposite(col):
		return 255 - int(col)
	values = col.split(',')
	output = ""
	k = 0
	for i in values:
		if k == 0:
			value = str(opposite(i[5:]))
			output = output + value + ','
		if k == 1 or k == 2:
			value = str(opposite(i))
			output = output + value + ','
		if k == 3:
			output = output + i
		k = k + 1
	return 'rgba('+output


if __name__ == "__main__":
	def dashrepl(matchobj):
		#print matchobj.group(0) #return convert(matchobj.group(0)[1:])
		return convert(matchobj.group(0))

	f = open('file.txt', 'r+')
	regex = re.compile("rgba\([0-9]+\,[0-9]+\,[0-9]+\,(\d*[.])?\d+\)", re.IGNORECASE)
	for line in f:
	    line = regex.sub(dashrepl, line)
	    print line
	#print convert('rgba(255,255,255,0.5)')
