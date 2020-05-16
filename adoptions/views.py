from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

# Create views
from .models import Pet

def home(request):
	# return HttpResponse('<p>home view</p>')
	pets = Pet.objects.all()
	return render(request, 'home.html', {'pets': pets})


def pet_detail(request, id):
	# return HttpResponse(f'<p>pet_detail view with the id {id}</p>')
	try:
		pet = Pet.objects.get(id=id)
	except Pet.DoesNotExists:
		raise Http404('Pet not found')
	return render(request, 'pet_detail.html', {'pet': pet})