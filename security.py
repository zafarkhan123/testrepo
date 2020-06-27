from werkzeug.security import safe_str_cmp
from user import User
users=[
	User(1,'bib','asd'),
	User(2,'bid','ad1'),
	User(3,'fid','ad2'),
]

username_mapping={ u.username : u for u in users}

userid_mapping= { u.id : u for u in users}

def username_authincate(username, password):
	user = username_mapping.get(username,None)
	if user and safe_str_cmp(user.password,password):
		return user

def identity(payload):
	user_id=payload['identity']
	return userid_mapping.get(user_id,None)


