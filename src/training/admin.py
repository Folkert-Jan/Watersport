from django.contrib import admin

# Register your models here.
from .forms import TrainingenForm
from .models import Trainingen


class TrainingenAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', "Locatie", "Datum"]
	form = TrainingenForm
		
	


	
admin.site.register(Trainingen, TrainingenAdmin)