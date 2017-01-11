from flask import Flask, request, render_template, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'somethingverysecret'

@app.route('/')
def home():
	#generate a random number
	random_num = int(random.random() * 100)
	#check if num is in session
	if 'num' not in session:
		session['num'] = random_num
	print session['num']
	return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
	guess = request.form['guess']
	guess = int(guess)
	if guess < session['num']:
		session['fail'] = "Too Low"
	elif guess > session['num']:
		session['fail'] = "Too High"
	else:
		if 'fail' in session:
			session.pop('fail')
		session['success'] = 'The number was {}.  You guessed it correctly'.format(session['num'])
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	#clear the session
	session.clear()
	#redirect to homepage
	return redirect('/')
app.run(debug=True)






