from django import forms 
from .models import apply
from .models import job 
class ApplyForm(forms.ModelForm):
    class  Meta:
        model = apply
        fields = ['name','email','website','cv','cover_letter'] 

class JobForm(forms.ModelForm):
    class  Meta:
        model = job
        fields = '__all__'
        exclude =('slug','owner')
