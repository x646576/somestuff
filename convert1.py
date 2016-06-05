import re
def convert(col):
	def opposite2(col):
		i = int(col, 16)
		y = int('ff', 16)
		return hex(y - i)

	def opposite1(col):
		i = int(col, 16)
		y = int('f', 16)
		return hex(y - i)
	def chunks(s, n):
	    for start in range(0, len(s), n):
	        yield s[start:start+n]
	s = '01234567890abcdef'
	if len(col) == 6:
		values = chunks(col, 2)
	else:
		values = chunks(col, 1)
	output = ""

	for i in values:
		if len(i) == 2:
			value = opposite2(i)[2:]
			output = output + value
		else:
			value = opposite1(i)[2:]
			output = output + value
	return '#'+output



if __name__ == "__main__":
	def dashrepl(matchobj):
		return convert(matchobj.group(0)[1:])

	f = open('input.css', 'r+')
	regex = re.compile(r"#[abcdef01234567890]+", re.IGNORECASE)
	for line in f:
	    line = regex.sub(dashrepl, line)
	    print line
