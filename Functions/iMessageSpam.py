from py_imessage import imessage

def spam(number, txtfile, numberoflines=False):
	txt = open(txtfile).read().strip()
	if not imessage.check_compatibility(number):
		print("Not an iPhone")
	txtlist = [i.strip() for i in txt.split('\n') if i != '']
	if numberoflines != False:
		if len(numberoflines) == 1:
			txtlist = txtlist[numberoflines[0]:]
		else:
			txtlist = txtlist[numberoflines[0]:numberoflines[1]]
	title = False
	for i in txtlist:
		if i != '':
			if i == i.upper() and title:
				i += ':'
			imessage.send(number, i)
			title = True

'''
txt = open('spam.txt').read().strip()
txtlist = [i.strip() for i in txt.split('\n') if i != '']
print(txtlist.index(string))
'''
spam("6788491617", 'spam.txt', [334])
