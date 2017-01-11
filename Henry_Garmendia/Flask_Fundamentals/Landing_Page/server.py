<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
=======
from flask import Flask, render_template
>>>>>>> upstream/master
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', name='Henry Garmendia')

@app.route('/ninjas')
def ninjas():
	return render_template('ninjas.html', name='Real Ninjas')

@app.route('/dojos/new')
def dojos():
	return render_template('dojos.html', name='Henry Garmendia | Real Ninja')

<<<<<<< HEAD
@app.route('/users', methods=['POST'])
def create_user():
	print "Got Post Info"
	# we'll talk about the following two lines after we learn a little more
	# about forms
	name = request.form['first_name']
	last = request.form['last_name']
	textarea = request.form['areatext']
	check = request.form['work']
	# redirects back to the '/' route
	return redirect('/')

app.run(debug=True)  # run our server
=======
app.run(debug=True)
>>>>>>> upstream/master
