from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static 



urlpatterns = [
    # Examples:
    # url(r'^$', 'Wva_vinkeveen.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


# // ADMIN
    url(r'^admin/', include(admin.site.urls)),

# // LOGIN
	url(r'^Home/', 'Login.views.Home', name='Home'),
	#url(r'^Forms', 'Login.views.contact', name='Forms'),

# // DJANGO REGISTRATION REDUX
	url(r'^accounts/', include('registration.backends.default.urls')),

# // OPDRACHTNE
	url(r'^Opdrachten/', 'Login.views.Opdrachten', name='Opdrachten'),

# // MEDIA
	url(r'^Media/', 'Login.views.Media', name='Media'),

# // TRAINING
	url(r'^Training/', 'training.views.Trainingen_function', name='Trainingen'),

# //HOUSE
	url(r'^$', 'Login.views.House', name='House'),
	




]

#if setting.DEBUG:
#	urlpatterns += static(setting.STATIC_URL, document_root=setting.STATIC_ROOT)
#	urlpatterns += static(setting.MEDIA_URL, document_root=setting.MEDIA_ROOT)