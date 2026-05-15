from django import forms
from .models import Thread,Reply
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ThreadForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    class Meta:
        model = Thread
        fields = ["title", "text", "image"]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a descriptive title'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Some more text under the post (optional)'
            })
        }
        labels = {
            'title': 'Thread Title',
            'text': 'Content'
        }

    def save(self, commit=True, author=None):
        thread = super().save(commit=False)
        if author:
            thread.author = author
        print("The thread is being SAVED!!!!!")
        if commit:
            thread.save()
            image = self.cleaned_data["image"]
            print("Image's here: ", image)
            if image:
                thread.image = image
                thread.save()
            return thread

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    icon = forms.ImageField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-group'}),
            'email': forms.EmailInput(attrs={'class': 'form-group'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = user.profile
            icon = self.cleaned_data["icon"]
            if icon:
                profile.icon = icon
                profile.save()
        return user

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["text"]

    def save(self, thread=None, commit=True, author=None):
        reply = super().save(commit=False)
        reply.thread = thread
        if author:
            reply.author = author

        print("The reply is being SAVED!!!!!")
        if commit:
            reply.save()
            return reply
