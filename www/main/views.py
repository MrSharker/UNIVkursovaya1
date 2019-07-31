from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import *
from .models import *

import json


def current_user(sess, request):
	sess['user_username']=request.session['user_username']
	sess['user_group']=request.session['user_group']


def home(request):
	session = {}
	with open('main/data/Reis.json', 'r', encoding='utf8') as file:
		text = json.loads(file.read())
	data = text["reiss"]
	data1 = DataBase()
	airports = data1.airports.get_list()
	try: 
		current_user(session, request)
	except: 
		print("We've got a bad news, sir")
		return redirect('auth')
	session['title'] = 'Рейсы'
	session['reiss'] = data
	session["airports"] = airports["airports"]
	return render(request, 'main/home.html', session)


def chr(request):
	try:
		if request.session['user_group'] == "moderator" or request.session['user_group'] == "admin":
			session = {}
			try:
				current_user(session, request)
			except:
				print("We've got a bad news, sir")
				return redirect('auth')
			session['title'] = 'Рейсы'

			data = DataBase()
			reiss = data.reiss.get_list()
			session["reiss"] = reiss["reiss"]
			if request.method == "POST":
				form = NewReis(request.POST)
				if "delete" in request.POST.keys():
					data.reiss.delete_reis(int(request.POST['delete']))
					session = data.reiss.get_list()
				elif "save" in request.POST.keys():

					if data.reiss.create_reiss( request.POST['cout'], request.POST['cin'], request.POST['timeout'], request.POST['timein'], request.POST['timefly'], request.POST['plane'], request.POST['status']):
						messages.success(request, f'Рейс добавлен')
					session = data.reiss.get_list
			else:
				form = NewReis()
			session = data.reiss.get_list()
			session['title'] = 'Рейсы'
			try:
				current_user(session, request)
			except:
				print("Sounds bad!")
			session['form'] = form
		else:
			return redirect('home')
	except:
		return redirect('home')
	return render(request, 'main/changeReis.html', session)


def chu(request):
	try:
		if request.session['user_group'] == "admin":
			session = {}
			try:
				current_user(session, request)
			except:
				print("Sounds bad")
				return redirect('auth')
			session['title'] = 'Управление пользователями'
			data = DataBase()
			users = data.users.get_list()
			session["users"] = users["users"]
			if request.method == "POST":
				if "delete" in request.POST.keys():
					data.users.delete_user(request.POST['delete'])
					session = data.users.get_list()
				if "give_pas" in request.POST.keys():
					user_update = request.POST.get("give_pas")
					data.users.new_group(user_update, "pas")
					if user_update == session['user_username']: request.session['user_group'] = "pas"

				elif 'give_admin' in request.POST.keys():
					user_update = request.POST.get("give_admin")
					data.users.new_group(user_update, "admin")
					if user_update == session['user_username']: request.session['user_group'] = "admin"

				elif "give_moderator" in request.POST.keys():
					user_update = request.POST.get("give_moderator")
					data.users.new_group(user_update, "moderator")

			session = data.users.get_list()
			session['title'] = 'Управление пользователями'
			try:
				current_user(session, request)
			except:
				print("Sounds bad!")
		else:
			return redirect('home')
	except:
		return redirect('home')
	return render(request, 'main/changeUser.html', session, )


def auth(request):
	data = DataBase()
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user_login = request.POST['login']
			user_pass = request.POST['password']
			current_u = data.users.auth(user_login, user_pass)
			if current_u:
				request.session['user_username'] = current_u.username
				request.session['user_group'] = current_u.group
				return redirect('home')
		else: print("ACHTUNG!")
	else: 
		try: 
			if request.session['user_username']: return redirect('home')
		except: form = LoginForm()
	return render(request, "main/auth.html", {'form': form, 'title': 'Авторизация'})


def reg(request):
	session = {}
	data = DataBase()
	users = data.users.get_list()
	session["users"] = users["users"]
	form = CreationForm()
	if "save" in request.POST.keys():
		if data.users.create_user(request.POST['username'], request.POST['password'], 'pas', request.POST['name'], request.POST['sername']):
			messages.success(request, f'Вы зарегистрировались')
		else:
			messages.error(request, f'...')
		session = data.users.get_list
		return redirect('auth')
	session = data.users.get_list()
	session['title'] = 'Авторизация'
	session['form'] = form
	return render(request, "main/auth/reg.html", session )


def exit(request):
	request.session.clear()
	return redirect('auth')