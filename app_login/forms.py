from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Senha")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}),label="Confirme a Senha")
    

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','email', 'password1', 'password2']  # Usuário só preenche email e senha
        

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email  # Definindo o username como o email
        if commit:
            user.save()
        return user
