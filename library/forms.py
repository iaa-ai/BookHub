from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'})
        }

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name','role','address']

class BookInstanceForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book','borrower', 'condition','check_out','check_in']
        widgets = {
            'check_out': forms.DateInput(attrs={'type': 'date'}),
            'check_in': forms.DateInput(attrs={'type': 'date'})
        }

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=50)

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your Password'})


class UserAddForm_Admin(UserCreationForm):
    is_staff = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm your Password'})
        self.fields['is_staff'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = self.cleaned_data['is_staff']
        if commit:
            user.save()
        return user

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user_image', 'user_bio']
