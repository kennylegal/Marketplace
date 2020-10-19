from django.contrib import messages
from django.contrib.auth.models import User
from django import forms
from .models import Comment
from django.contrib.auth.forms import UserCreationForm


# class Userform(UserCreationForm):
#     class Meta:
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'username',
#             'email',
#             'password1',
#             'password2'
#         ]
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         mail = User.objects.filter(email__iexact=email)
#         if mail.exists():
#             raise forms.ValidationError('Email has already been used')
#         return email


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'comment'
        ]
