import urllib.request
from bs4 import BeautifulSoup

def allanagrams(s):
	possible = [i for i in s if i in 'ai']
	anagrams = list(s)
	for i in range(len(s)-1):
		new = []
		for j in anagrams:
			possadd = list(s)
			for k in j:
				possadd.remove(k)
			for m in possadd:
				newstr = j + m
				if len([i for i in newstr if i in 'aeiouy']) > 0:
					possible += [newstr]
				new += [newstr]
		anagrams += new
	return set(possible)


# help find indices of all starting letters
'''
let, counter = 0, 0
positions = dict.fromkeys(letters, 0)
for i in range(len(allwords)):
	try:
		if allwords[i].lower()[0] == letters[let]:
			positions[letters[let]] = i
			let += 1
	except Exception as e:
		pass
'''

def possanagrams(word, removeuseless=False):
	x = open('englishwords.txt', 'r')
	allwords = [i.rstrip(' .-\n').lower() for i in x.readlines()]
	letters = 'abcdefghijklmnopqrstuvwxz'
	x.close()

	# letter index found by above code, but y-words are mixed with i-words
	letterindex = [36, 30886, 55218, 94151, 116930, 133746, 149616, 164082, 182744, 199705, 203863, 210030, 224124, 249322, 265497, 280559, 321516, 324734, 346021, 396605, 421838, 445630, 452447, 464119, 464728]
	letterdict = {0: allwords[:36], 'z': allwords[464728:]}
	for i in range(len(letterindex) - 1):
		letterdict[letters[i]] = allwords[letterindex[i]: letterindex[i+1]]
	iwords = []
	ywords = []
	for i in letterdict['i']:
		if i.lower()[0] == 'i':
			iwords += [i]
		elif i.lower()[0] == 'y':
			ywords += [i]
	letterdict['i'] = iwords
	letterdict['y'] = ywords
	others = []
	for i in list(letterdict.keys())[1:]:
		for j in letterdict[i]:
			if j.lower()[0] != i:
				others += [j]
				letterdict[i][letterdict[i].index(j)] = ''
		letterdict[i] = list(filter(lambda a: a != '', letterdict[i]))
	letterdict['others'] = others

	anagramlist = allanagrams(word)
	poss = []
	for i in anagramlist:
		if i in letterdict[i.lower()[0]]:
			poss += [i]

	if removeuseless:
		# searches each word on Merriam-Webster
		# if word is not found in the dictionary or if the word is a part of speech or type of word that is not accepted, like 'U.S. Case Law', 'biographical name', 'prefix', 'abbreviation', 'combining form', 'geographical name', 'symbol', 'abbreviation (1)'
		possibilities = []
		for i in poss:
			url = 'https://www.merriam-webster.com/dictionary/' + i
			try:
				htmlfile = urllib.request.urlopen(url)
				# class_ = 'dtText' gives definition of word
				soup = BeautifulSoup(htmlfile, 'lxml')
				soup1 = soup.find(class_='dtText')
				if soup1 == None:
					possibilities += [i]
				definition = soup1.get_text().split(': ')[-1]
				exist = soup.find(class_='fl')
				wordtype = exist.text.strip()
				if wordtype not in ['U.S. Case Law', 'biographical name', 'prefix', 'abbreviation', 'Law', 'combining form', 'geographical name', 'symbol', 'abbreviation (1)', 'interjection', 'noun suffix', 'noun combining form']:
					possibilities += [i]
			except Exception as e:
				pass
			poss = list(possibilities)

	lengths = dict.fromkeys(range(1, len(word)+1), [])
	for i in poss:
		lengths[len(i)] = lengths[len(i)] + [i]
	for i in range(1, len(word)):
		lengths[i] = sorted(lengths[i])
	return lengths