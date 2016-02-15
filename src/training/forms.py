from django import forms 
from .models import Trainingen





class TrainingenForm(forms.ModelForm):
	class Meta:
		model = Trainingen
		fields = ['Klasse','Locatie', 'Datum']
		


		