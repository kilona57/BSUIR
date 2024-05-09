from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import StanderUser, Manager, StuffMember, Customer, Product, Company, Order, CustomerOrder
import mysite.settings as s

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Имя'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Фамилия'}))

	class Meta(User):
		model = User
		fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['personal number'].widget.attrs['class'] = 'form-control'
		self.fields['personal number'].widget.attrs['placeholder'] = 'User Name'
		self.fields['personal number'].label = ''
		self.fields['personal number'].help_text = '<ul class="form-text text-muted small"><li>Пользователь с таким персональным номером уже существует.</li><li>Обязательно. 150 символов и менее. Только буквы, цифры и @/./+/-/_ .</li></ul>'

		self.fields['access'].widget.attrs['class'] = 'form-control'
		self.fields['access'].widget.attrs['placeholder'] = 'Password'
		self.fields['access'].label = ''
		self.fields['access'].help_text = '<ul class="form-text text-muted small"><li>Ваш пароль не должен повторять ваши данные.</li><li>Пароль должен содержать 8 и более символов.</li><li>Пароль слишком легко угадать.</li><li>Пароль не должен состоять только из цифр.</li></ul>'

class AuthorizationForm(forms.ModelForm):
	personal_number = forms.IntegerField(required=True, label="", widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Персональный номер'}))
	class Meta:
		model = StanderUser
		exclude = ('user',)


class AddBudgetForm(forms.ModelForm):
	name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Название'}))
	limit = forms.FloatField(required=True, label ='',widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Лимит'}))
	class Meta:
		model = Budget
		exclude = ('user',)

class AddTransactionForm(forms.ModelForm):
	#sum = forms.FloatField(required=True, label ='',widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cумма'}))
	category = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'категория бюджета'}))
	#data = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label ='',widget=forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Дата и время'}))
	class Meta:
		model = Transaction
		exclude = ('user',)

class AddIncomeForm(forms.ModelForm):
	name = forms.CharField(required=True, label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Название'}))
	sum = forms.FloatField(required=True, label ='',widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Cумма'}))
	time = forms.DateField(required=True, input_formats=s.DATE_INPUT_FORMATS, label ='',widget=forms.DateInput(attrs={'class':'form-control', 'placeholder':'Дата начисления'}))
	class Meta:
		model = Income
		exclude = ('user',)