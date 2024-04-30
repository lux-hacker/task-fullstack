from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Логин")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class RegistrationForm(forms.Form):
    username = forms.CharField(label="Логин")
    name = forms.CharField(label="Фамилия Имя Отчество")
    password = forms.CharField(widget=forms.PasswordInput, label="Придумайте пароль")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Повторите пароль")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароль не совпадают')
        return cd['password2']
