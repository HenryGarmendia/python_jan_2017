from flask import Flask, request, redirect, render_template, session, flash
import re

from mysqlconnection import MySQLConnector
app = Flask(__name__)

app.secret_key = 'specialpassword'

mysql = MySQLConnector(app, 'fullfriends')

VALIDATOR = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	# get all my friends from DB
	query = 'SELECT * FROM friends'
	friends = mysql.query_db(query)

	return render_template('index.html', all_friends=friends, name='Henry Garmendia')

@app.route('/friends', methods=['POST'])
def create():
	# create a pattern to remember
	is_valid = True
	# validation, if the validation fails, redirect to /index
	if len(request.form['first_name']) == 0:
		flash('* First name is required', 'registration');
		is_valid = False;

	if len(request.form['last_name']) == 0:
		flash('* Last name is required', 'registration');
		is_valid = False;

	#validate email

	if not is_valid:
		return redirect('/')

	# once validated put user in the DB 
	query = 'INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW());'
	data = {
			'first_name':	request.form['first_name'],
			'last_name':	request.form['last_name'],
			'email':		request.form['email'],
	}

	# this is to run the query once we put in the data dictionarie
	mysql.query_db(query, data)

	# reditect to /index
	return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
	query = 'SELECT * FROM friends WHERE id=:id'
	data = {
			'id': id,
	}

	friends = mysql.query_db(query, data)

	if len(friends) is 0:
		return redirect('/')
	#I'm certain that friends is not empty and pass it in the template
	friend = friends[0]
	# need to get the id from the edit button and send it to the template with the same id
	return render_template('edit.html', id=id, all_friends=friends, friend=friend, name='Henry Garmendia')

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	
	is_valid = True
	# validate the form
	if len(request.form['first_name']) == 0:
		flash('* First name is required', 'registration');
		is_valid = False;

	if len(request.form['last_name']) == 0:
		flash('* Last name is required', 'registration');
		is_valid = False;

	#validate email

	if not is_valid:
		# this will return the user to the same form if the messup editing this form
		return redirect('/friends'+id+'/edit')

	# update the DB with new user information
	query = 'UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id';

	data = {
			'first_name':	request.form['first_name'],
			'last_name':	request.form['last_name'],
			'email':		request.form['email'],
			'id':			id,
	}

	mysql.query_db(query, data)

	#redirect to the main page
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	query = 'DELETE FROM friends WHERE id=:id'
	data = {
			'id': id,
	}

	mysql.query_db(query, data)

	return redirect('/')


app.run(debug=True)

















































