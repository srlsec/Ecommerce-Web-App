from django import forms
from store.models import Order, Customer, Product
from django.contrib.auth.models import User


class CustomerRegistrationForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = Customer
        fields = ["username", "password", "email", "full_name", "address"]

    def clean_username(self):
        uname = self.cleaned_data.get("username")
        if User.objects.filter(username=uname).exists():
            raise forms.ValidationError(
                "Customer with this username already exists.")

        return uname
        
