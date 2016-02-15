from django.shortcuts import render

# Create your views here.
from .forms import TrainingenForm
from training.models import Trainingen

def Trainingen_function(request):
	title = "mytitle"
	form = TrainingenForm(request.POST or None)	


	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		form = TrainingenForm()

	context = {
		"template_title": title,
		"form" : form, 
		
	}



	return render(request, "Training.html" , context)


def trainingen_get(request):

	Trainingen = Trainingen.objects.all()

	context = {
		"Trainingen" : trainingen, 
		
	}


	return render(request, "Training.html" , context)