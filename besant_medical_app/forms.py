from django import forms
from .models import RegisterData,Medstoringsupplier,Medmedicalshop,Supquantmanagmnt,Medicalquantmgnt
from multiselectfield import MultiSelectField

CUSTOMER_TYPE = [
        ('Admin', 'Admin'),
        ('Supplier', 'Supplier'),
        ('Customer', 'Customer')
    ]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    customer = forms.ChoiceField(choices=CUSTOMER_TYPE,widget=forms.RadioSelect())
    class Meta:
        model = RegisterData
        fields = ['first_name','last_name','username','password','password2','email','mobile','customer']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    customer = forms.ChoiceField(choices=CUSTOMER_TYPE, widget=forms.RadioSelect())
    class Meta:
        model = RegisterData
        fields = ['username','password','customer']



class medstoringsupForm(forms.ModelForm):
    class Meta:
        model = Medstoringsupplier
        fields = '__all__'

class medmedicalshopForm(forms.ModelForm):
    class Meta:
        model = Medmedicalshop
        fields = '__all__'

class supquantmanagmntForm(forms.ModelForm):
     class Meta:
        model = Supquantmanagmnt
        fields = '__all__'


class medicalquantmgntForm(forms.ModelForm):
    class Meta:
        model = Medicalquantmgnt
        fields = '__all__'