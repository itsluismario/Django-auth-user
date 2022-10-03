from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import User

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=32,required=True, label=('Nombre'),
                           widget= forms.TextInput
                           (attrs={'type':'text','class':'form-control col-sm-6"',
				                   'name':'fullName','id':'fullNameSrEmail','placeholder':'Carlos',
                                   'aria-label':'Carlos','data-msg':'Pon tu nombre.','autocomplete':'off'}))

    last_name = forms.CharField(max_length=32,required=True, label=('Apellido'),
                           widget= forms.TextInput
                           (attrs={'type':'text','class':'form-control',
				                   'placeholder':'Federer',
                                   'aria-label':'Federer','data-msg':'Please write your last name.','autocomplete':'off'}))

    email = forms.CharField(max_length=32,required=True, label=('Email'),
                           widget= forms.TextInput
                           (attrs={'type':'email','class':'form-control',
				                   'name':'email','id':'signupSrEmail','placeholder':'federer@ejemplo.com',
                                   'aria-label':'Federer@example.com','data-msg':'Please write your email.'}))

    password1 = forms.CharField(max_length=100,required=True,label=('Password'),
                           widget= forms.TextInput
                           (attrs={'type':'password', 'class':"js-toggle-password form-control form-control-lg", 'name':"password", 'id':"signupSrConfirmPassword", 'placeholder':"8+ caracteres requeridos", 'aria-label':"8+ caracteres requeridos", 'required minlength':"8",
                           'data-hs-toggle-password-options':'{"target": [".js-toggle-password-target-1", ".js-toggle-password-target-2"],"defaultClass": "bi-eye-slash","showClass": "bi-eye", "classChangeTarget": ".js-toggle-password-show-icon-2"}'}))

    password2 = forms.CharField(max_length=100,required=True,label=('Confirm Password'),
                           widget= forms.TextInput
                           (attrs={'type':'password', 'class':"js-toggle-password form-control form-control-lg", 'name':"confirmPassword", 'id':"signupSrConfirmPassword", 'placeholder':"8+ caracteres requeridos", 'aria-label':"8+ caracteres requeridos", 'required minlength':"8",
                           'data-hs-toggle-password-options':'{"target": [".js-toggle-password-target-1", ".js-toggle-password-target-2"],"defaultClass": "bi-eye-slash","showClass": "bi-eye", "classChangeTarget": ".js-toggle-password-show-icon-2"}'}))

    cc_myself = forms.BooleanField(required=True,
                                    widget= forms.TextInput
                                    (attrs={'type':'checkbox','class':'form-check-input','autocomplete':'off'}))


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name','email','password1','password2','cc_myself']

    def clean(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('password_confirm'):
            self.add_error('password_confirm', "passwords do not match !")
        return cd

class UserLoginForm(forms.ModelForm):
    email = forms.CharField(max_length=32,required=True,
                               widget= forms.TextInput
                               (attrs={'type':'email','class':'form-control',
    				                   'name':'email','placeholder':'federer@ejemplo.com',
                                       'aria-label':'federer@example.com','data-msg':'Correo inválido.'}))

    password = forms.CharField(max_length=100,required=True,
                           widget= forms.TextInput
                           (attrs={'type':'password','class':'form-control','autocomplete':'off',
				                   'name':'password','placeholder':'8+ caracteres requeridos',
                                   'aria-label':'8+ caracteres requeridos',
                                   'data-hs-toggle-password-options':'{"target": [".js-toggle-password-target-1", ".js-toggle-password-target-2"],"defaultClass": "tio-hidden-outlined","showClass": "tio-visible-outlined", "classChangeTarget": ".js-toggle-passowrd-show-icon-1"}'}))

    # password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('email','password')


from django.contrib.auth.forms import PasswordResetForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'type': 'email',
        'name': 'email',
        'data-msg':'Correo inválido.'
        }))

