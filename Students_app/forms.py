from django import forms
from .models import Students
from django.core.exceptions import ValidationError

def age_validator(value):
    if value <1:
        raise ValidationError("Age must be greater than 0")
    elif value >=130:
        raise ValidationError("Age can not be more than 130")
    else:
        pass   

def img_validator(value):
    if value.name.lower() == "sad.jpg":
        raise ValidationError("Photo daal bhai")
    
class StudentsForm(forms.ModelForm):
    age = forms.IntegerField(validators = [age_validator])
    img = forms.FileField(validators=[img_validator])
    class Meta:
        model = Students
        fields = ["name","email","age","img"]
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
        #     'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
        #     'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        # }

        

    # name = forms.CharField(max_length=100, min_length = 3)
    # age = forms.IntegerField()
    # email = forms.EmailField(unique = True, )
