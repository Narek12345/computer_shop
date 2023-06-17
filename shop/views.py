from django.shortcuts import render
from .models import Computer


def main(request):
	computers = Computer.objects.all()

	context = {'computers': computers}
	return render(request, 'shop/main.html', context)