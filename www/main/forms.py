from django import forms


class LoginForm(forms.Form):
	login = forms.CharField(label="Логин", required=True, max_length=50)
	password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput(), max_length=150)


class CreationForm(forms.Form):
	username = forms.CharField(label="Логин", required=True, widget = forms.TextInput(attrs={'placeholder': "Логин пользователя..."}), max_length=50)
	password = forms.CharField(label="Пароль", required=True, widget=forms.PasswordInput(attrs={'placeholder': "Пароь пользователя..."}), max_length=150)
	name = forms.CharField(label="Имя", required=True, widget = forms.TextInput(attrs={'placeholder': "Имя пользователя..."}), max_length=50)
	sername = forms.CharField(label="Фамилия", required=True, widget = forms.TextInput(attrs={'placeholder': "Фамилия пользователя..."}), max_length=50)


class NewReis(forms.Form):
	cout = forms.CharField(label="Город вылета", required=True, max_length=50, widget = forms.TextInput(attrs={'placeholder': "Город 1"}),)
	cin = forms.CharField(label="Город прилета", max_length = 50, required=True, widget=forms.TextInput(attrs={'placeholder': "Город 2"}))
	timeout = forms.CharField(label="Время вылета", required=True,max_length=5, widget= forms.TextInput(attrs={'placeholder': "Время 1"}),)
	timein = forms.CharField(label="Время прибытия", required=True, max_length=5, widget=forms.TextInput(attrs={'placeholder': "Время 2"}),)
	timefly = forms.CharField(label="Время полета", required=True, max_length=40, widget=forms.TextInput(attrs={'placeholder': "Время 3"}),)
	plane = forms.ChoiceField(label="Тип самолета", widget=forms.Select(), choices=([('А321','А321'), ('A320','A320'), ('B735','B735'),('BCS3', 'BCS3') ]), required = True)
	status = forms.ChoiceField(label="Статус рейса", widget=forms.Select(), choices=([('Регистрация', 'Регистрация'), ('Посадка', 'Посадка')]), required=True)
