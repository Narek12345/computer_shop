from django.contrib import admin

from .models import Computer


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
	
	# Отображаем нужные атрибуты в admin panel.
	list_display = ('name', 'category')

	# Создаем нужные фильтры в admin panel.
	list_filter = ('price',)

	# Задаем поля, по которым будет идти поиск в случае запросов.
	search_fields = ('name',)

	def get_form(self, request, obj=None, **kwargs):
		form = super().get_form(request, obj, **kwargs)
		form.base_fields['name'].label = 'Name (only computer!):'
		return form