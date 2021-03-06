from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField(label='Email address', max_length = 100)
    first_name = forms.CharField(max_length=50, label='First name')
    last_name = forms.CharField(max_length=50, label='Last name')

    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()