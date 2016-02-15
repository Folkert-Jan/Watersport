from django.db import models

# Create your models here.

class Trainingen(models.Model):

	KLASSE = (
		('Opt','Optimist'),
		('Spl','Splash'),
		('Lsr','Laser'),
		('Fv', 'Rs Feva'),
		('500','Rs 500'),
		('29', '29er'),
		)


	Klasse = models.CharField(max_length=3 , choices=KLASSE)
	Locatie = models.CharField(max_length=120, verbose_name="Locatie")
	Datum = models.CharField(max_length=120, verbose_name="Datum")
	# MeerInfo = models.TextField(max_length=400)

	def __unicode__(self):
		return self.Klasse
 	