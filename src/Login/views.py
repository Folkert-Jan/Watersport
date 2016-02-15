from django.shortcuts import render
from .forms import SignUpForm
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.


def Home(request):
	

	#add a form
	form = SignUpForm(request.POST or None) 
	context = {
	 
		"form": form
	}
	
	if form.is_valid():	

		instance = form.save(commit=False)
	
		full_name = form.cleaned_data.get("full_name") 
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name

		instance.save()
		context = {
			"title": "Thank you"
		}


	return render(request, "Home.html", context)



def Trainingen(request):

	return render(request, "Trainingen.html", {} )

def House(request):

	return render(request, "House.html", {} )

def Opdrachten(request):

	return render(request, "Opdrachten.html", {} )

def Media(request):

	return render(request, "Media.html", {} )




















