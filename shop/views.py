from django.views import generic
from django.shortcuts import render

from .models import Computer


def index(request):

	return render(request, 'shop/index.html')


class ComputerListView(generic.ListView):
	model = Computer
	paginate_by = 10
	

class ComputerDetailView(generic.DetailView):
	model = Computer