from django.urls import path
from . import views

urlpatterns = [
	path('reg/', views.home, name='home'),
	path('reg/verification/<str:email>/<int:code>', views.verification, name='verification'),
	path('reg/next/', views.registration, name='registration'),
	path('ajax/load-languages/', views.load_languages, name='ajax_load_languages'),
	path('reg/thanks',views.thanks_view, name='thanks_view'),

	# path('confirm/', views.OrganisationView.as_view(), name='organisation'),

]
