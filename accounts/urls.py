from . import views
from django.urls import path, include


app_name = 'accounts'
urlpatterns = [
	# Включить URL авторизаций по умолчанию.
	path('', include('django.contrib.auth.urls')),
	# Выход из аккаунта.
	path('logout/', views.logout, name='logout'),
	# Регистрация.
	path('register/', views.register, name='register'),
	# Профиль пользователя.
	path('profile/', views.profile, name='profile'),
]