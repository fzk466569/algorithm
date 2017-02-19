# _*_ coding: utf-8 _*_
__author__ = 'fzk'
__date__ = '2017/2/19 0019 13:51'


def hashstring(string):
	length = len(string)
	if length == 0:
		return
	i = 0
	j = 0
	tempstring = ''
	while i < length:
		while i < length and string[i] == string[j]:
			i += 1
		tempstring += string[j]
		tempstring += str(i - j)
		j = i
	if len(tempstring) >= length:
		return string
	else:
		return tempstring
	return string

if __name__ == "__main__":
	string = 'aasdssddfffggcccccc'
	print hashstring(string)

