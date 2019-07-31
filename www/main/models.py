import json
import hashlib


class DataBase:
	def __init__(self):
		self.users = Users()
		self.reiss = Reiss()
		self.airports = Airports()

class User:
	def __init__(self, id, username, password, group, name, sername):
		self.username = username
		self.password = password
		self.id = id
		self.group = group #pas/moderator/admin
		self.name = name
		self.sername = sername


class Users:
	def __init__(self):
		self.path = 'main/data/users.json'
		self.users = []
		self.load_js()

	def save(self):
		with open(self.path, 'w', encoding="utf-8") as file: json.dump(self.get_list(), file)

	def load_js(self):
		with open(self.path, 'r', encoding="utf-8") as file:
			text = json.loads(file.read())
		for each in text["users"]: self.users.append(User(each["id"],each["username"],each["password"],each["group"], each["name"], each["sername"]))

	def auth(self, username, password):
		password = password[:int(len(password) / 2)] + str(username) + password[int(len(password) / 2):]
		byted = bytes(password, "utf-8")
		hashed = hashlib.sha1(byted)
		password = hashed.hexdigest()
		for user in self.users:
			if (user.username == username) and (user.password == password): return user

	def create_user(self, username, password, group, name, sername):
		password = password[:int(len(password) / 2)] + str(username) + password[int(len(password) / 2):]
		byted = bytes(password, "utf-8")
		hashed = hashlib.sha1(byted)
		password = hashed.hexdigest()
		ids = []
		users = self.get_list()["users"]

		for each in users: ids.append(each["id"])
		if len(ids) == 0:
			user_id = 0
		else:
			user_id = max(ids) + 1
		for each in self.users:
			if username == each.username:
				return False
		else:
			self.users.append(User(user_id, username, password, group, name, sername ))
			self.save()
			return True

	def get_list(self):
		data = []
		for each in self.users:
			data.append({"id": each.id, "username": each.username, "password": each.password, "group": each.group, "name": each.name, "sername": each.sername})
		return {"users": data}

	def new_group(self, username, newGroup):
		for each in self.users:
			if each.username == username:
				each.group = newGroup
				self.save()
				return each.group

	def delete_user(self, username):
		for each in self.users:
			if each.username == username:
				self.users.remove(each)
				self.save()
				break


class Reis:
	def __init__(self, nom, cout, cin, timeout, timein, timefly, plane, status):
		self.nom = nom
		self.cout = cout
		self.cin = cin
		self.timeout = timeout
		self.timein = timein
		self.timefly = timefly
		self.plane = plane
		self.status = status


class Reiss:
	def __init__(self):
		self.path = 'main/data/Reis.json'
		self.reiss = []
		self.load()

	def load(self):
		with open(self.path, 'r', encoding="utf-8") as file:
			text = json.loads(file.read())
		for each in text["reiss"]: self.reiss.append(
			Reis(each["nom"], each["cout"], each["cin"], each["timeout"], each["timein"], each["timefly"], each["plane"], each["status"]))

	def save(self):
		with open(self.path, 'w', encoding="utf-8") as file: json.dump(self.get_list(), file)

	def create_reiss(self, cout, cin, timeout, timein, timefly, plane, status):
		ids = []
		reiss = self.get_list()["reiss"]
		for each in reiss: ids.append(int(each['nom']))
		if len(ids) == 0: reiss_nom = 0
		else:
			reiss_nom = max(ids)+1
		self.reiss.append(Reis(reiss_nom, cout, cin, timeout, timein, timefly, plane, status))
		self.save()

	def delete_reis(self, nom):
		for each in self.reiss:
			if each.nom == nom:
				self.reiss.remove(each)
				self.save()
				break

	def get_list(self):
		data = []
		for each in self.reiss:
			data.append({"nom": each.nom, "cout": each.cout, "cin": each.cin, "timeout": each.timeout, "timein": each.timein, "timefly": each.timefly, "plane": each.plane, "status": each.status})
		return {"reiss": data}


class Airport:
	def __init__(self,id, name, city):
		self.id = id
		self.name = name
		self.city = city

class Airports:
	def __init__(self):
		self.path = 'main/data/Airports.json'
		self.airports = []
		self.load()

	def load(self):
		with open(self.path, 'r', encoding="utf-8") as file:
			text = json.loads(file.read())
		for each in text["airports"]: self.airports.append(Airport(each["id"], each["name"], each["city"]))

	def get_list(self):
		data = []
		for each in self.airports:
			data.append({"id": each.id, "name": each.name, "city": each.city})
		return {"airports": data}