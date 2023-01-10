from flask import Flask, render_template, request, redirect, abort
from solveanagram import possanagrams

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/connect", methods=["POST"])
def connect():
	if request.method == "POST":
		x = request.form["letters"]
		letters = ''.join([i for i in x if i.isalpha()])
		realfilter = request.form["filter"]
		return redirect(f"/{letters}/{realfilter}")

@app.route("/<letters>/<realfilter>")
def dataPage(letters, realfilter):
	filterbool = realfilter == 'Yes'
	letterData = possanagrams(letters, filterbool)
	for i in letterData.keys():
		letterData[i] = ' '.join([i for i in letterData[i]])
	if letterData:
		return render_template("wordpage.html", title=letters, wordlist=letterData)
	return abort(404)

'''
@app.route('/', methods = ["POST", "GET"] )
def home():
	inputword=request.
	words = possanagrams(inputword)
	for i in words.keys():
		words[i] = ' '.join([i for i in words[i]])
	return render_template('home.html', wordlist = words, title = inputword.upper())


@app.route('/forms', methods=['POST', 'GET'])
def anagramsubmit():
	# = SubmitAnagram()
	return render_template('formsubmit.html')
'''

if __name__ == '__main__':
	# use local IP address for host to access on trusted devices home: '192.168.1.82', school: '10.41.204.25'
	app.run(debug=True)
	# , host= '10.41.204.25'