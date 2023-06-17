"""Links to the 'shop' app"""

from . import views
from django.urls import path


app_name = 'shop'
urlpatterns = [
	# Главная страница.
	path('', views.main, name='main'),
]