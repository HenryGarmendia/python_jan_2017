from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name='Henry Garmendia')

@app.route('/result')
def result():
	return render_template('result.html')

@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	# we'll talk about the following two lines after we learn a little more
	# about forms
	fullName = request.form['full_name']
	cityLoc = request.form['location']
	favLang = request.form['fav-track']
	textArea = request.form['areatext']
	# redirects back to the '/' route
	return render_template('result.html', full_Name=fullName, city_Loc=cityLoc, fav_Lang=favLang, comment=textArea)



	

app.run(debug=True)  # run our server