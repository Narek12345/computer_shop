"""Links to the 'shop' app"""

from . import views
from django.urls import path


app_name = 'shop'
urlpatterns = [
	# Главная страница.
	path('', views.index, name='index'),
	# Страница со списком всех компьютеров.
	path('computers', views.ComputerListView.as_view(), name="computers"),
	# Страница с информацией о конкретном компьютере.
	path('computer/<pk>', views.ComputerDetailView.as_view(), name="computer-detail"),
]