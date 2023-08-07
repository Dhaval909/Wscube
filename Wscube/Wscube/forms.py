from django import forms 

#inherit class
class UserForm(forms.Form):
    num_1=forms.CharField(label='value-1',required=False, widget=forms.TextInput(attrs={'class':'form-control'}))
    num_2= forms.CharField(label='value-2')