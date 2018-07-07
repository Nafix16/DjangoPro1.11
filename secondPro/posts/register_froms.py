from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registration(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        # model2 = Post
        fields = {
            'username',
            'email',
            'password1',
            'password2',
        }

        def save(self, commit=True) :
            user = super(Registration, self).save(commit=False)
            user.first_name = self.cleaned_data('first_name')
            user.last_name = self.cleaned_data('last_name')
            user.email = self.cleaned_data('email')
            user.password1 = self.cleaned_data('password1')
            user.password2 = self.cleaned_data('password2')

            if commit:
                user.save()
                return user








