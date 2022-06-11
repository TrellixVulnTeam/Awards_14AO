from django import forms
from .models import Project,Profile,Review, RATE_CHOICES

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture','username','bio','email','phone_number'] 

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=['title','image','description','country','link']         

class RateForm(forms.ModelForm):
    design = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    usability = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    content = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)
    
    class Meta:
        model = Review
        fields=['design','usability','content','comment']   
  