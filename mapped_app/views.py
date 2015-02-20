from django.shortcuts import render
from mapped_app.models import Location


# with GoogleMaps
def home(request):
	company_list = Location.objects.all()
	context_dict = {'company_list': company_list}
	#return render(request, 'mapped/home.html', context_dict)
	return render(request, 'mapped/home.html', context_dict)


# with OpenStreetMap
def open(request):
	return render(request, 'mapped/OSM.html', {})


# with Leaflet
def leaf(request):
	return render(request, 'mapped/leaflet.html', {})


# with OpenLayer
def openlayer(request):
	return render(request, 'mapped/openlayer.html', {})