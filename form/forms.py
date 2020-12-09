from django import forms


class CreateNewForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    phone_number = forms.IntegerField(label="Phone Number")
    email = forms.EmailField(label="Email", max_length=200)
    comments = forms.CharField(label="Comments", max_length=500)
