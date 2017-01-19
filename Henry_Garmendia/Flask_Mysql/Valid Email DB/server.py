from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)

app.secret_key = 'specialpassword'

mysql = MySQLConnector(app,'emailvaliddb')

VALIDATOR = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	query = 'SELECT * FROM emails'														# define your query
	email = mysql.query_db(query)														# run query with query_db()

	return render_template('index.html', all_emails=email, name='Henry Garmendia')		# pass data to our template

@app.route('/submit_email', methods=['POST'])
def submit_email():
	email = request.form['email']

	if len(email) == 0:
		flash('* Name cannot be blank', 'registration')
		
		return redirect('/')
	elif not VALIDATOR.match(email):
		flash('* Email is not valid!', 'registration')
		
		return redirect('/')
	else:
		query = 'INSERT INTO emails (email, created_at, updated_at) VALUES (:email, NOW(), NOW());'

		data = {
				'email': email
		}
		mysql.query_db(query, data)
	return redirect('/')

@app.route('/delete_email/<emails_id>', methods=['POST'])
def delete_email(emails_id):
	query = 'DELETE FROM emails WHERE id = :emails_id'
	data = {
			'emails_id': emails_id
	}
	mysql.query_db(query, data)
	return redirect('/')

app.run(debug=True)


































