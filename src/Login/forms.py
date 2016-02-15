from django import forms
from .models import SignUp



class SignUpForm(forms.ModelForm):
	class Meta:

		model = SignUp
		fields = ["First_Name", "Last_Name", "Email"] 