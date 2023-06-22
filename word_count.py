str = input('Enter a sentence or a paragraph:\n')
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in str:
	if i in punc:
		str = str.replace(i, '')
str = str.lower()
str = str.split(' ')
str_dict = {}
for word in str:
	str_dict[word] = 0
for word in str:
	for key in str_dict.keys():
		if word == key:
			str_dict[word] += 1	


for key in sorted(str_dict):
	print(key,':',str_dict[key])

	