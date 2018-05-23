from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db' 
os.path.join(basedir, 'crud.sqlite')
db = SQLAlchemy(app)
ma = Marshmallow(app)



class User(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
	password = db.Column(db.String(80), unique=True)


	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password


class UserSchema(ma.Schema):
	class Meta:
		#fields to expose
		fields = ('username', 'email', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


#endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
	username = request.json['username']
	email = request.json['email']
	password = request.json['password']

	new_user = User(username, email, password)
	db.session.add(new_user)
	db.session.commit()
	return jsonify(new_user)

#endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
	all_users = User.query.all()
	result = users_schema.dump(all_users)
	return jsonify(result.data)


#endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def get_user_byId(id):
	user = User.query.get(id)
	return user_schema.jsonify(user)



#endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def update_user(id):
	user = User.query.get(id)
	username = request.json['username']
	email = request.json['email']
	password = request.json['password']

	user.email = email
	user.username = username
	db.session.commit()
	return user_schema.jsonify(user)



#endpoint to del user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
	user = User.query.get(id)
	db.session.delete(user)
	db.session.commit()
	return user_schema.jsonify(user)

if __name__ == '__main__':
	app.run(debug=True)
















		