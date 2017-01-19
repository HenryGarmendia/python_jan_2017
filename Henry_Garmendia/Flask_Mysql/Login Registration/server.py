from flask import Flask, session, render_template, redirect, flash, request
from flask_bcrypt import Bcrypt
from mysqlconnection import MySQLConnector


app = Flask(__name__)
app.secret_key = 'specialpassword'
bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'flask_login_reg')


@app.route('/')
def index():
	return render_template('index.html', name='Henry Garmendia')

@app.route('/users', methods=['POST'])
def create():
	name 		= request.form['name']
	email 		= request.form['email']
	password 	= request.form['password']

	is_valid = True
	if len(name) == 0:
		flash('* Name cannot be blank', 'registration')

		is_valid = False
	if len(email) == 0:
		flash('* Email cannot be blank', 'registration')

		is_valid = False
	if len(password) < 3:
		flash('* Password must be at least three characters', 'registration')

		is_valid = False

	if is_valid:
		# save to DB
		hashed_pw = bcrypt.generate_password_hash(password)
		query = 'INSERT INTO users (name, email, password, created_at, updated_at) VALUES (:name, :email, :password, NOW(), NOW());'

		data = {
				'name': 	name,
				'email':	email,
				'password':	hashed_pw,
		}

		mysql.query_db(query, data)
		return redirect('/success')
	else:
		# redirect to registration page and show errors
		return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']

	# check if there is a user on the DB with credential provided
	query = 'SELECT * FROM users WHERE email = :email;'
	data = {'email': email}

	# we need the DB to send it back to us, so well create an user object
	user = mysql.query_db(query, data)
	# need to find in our DB the user and authenticate there password
	if len(user) and bcrypt.check_password_hash(user[0]['password'], password):
		return redirect('/success')
	else:
		flash('Invalid credentials.', 'login')
		return redirect('/')

app.run(debug=True)








































