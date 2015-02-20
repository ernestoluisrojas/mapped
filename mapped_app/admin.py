from django.contrib import admin
from mapped_app.models import Location

class LocationAdmin(admin.ModelAdmin):
	class Meta:
		model = Location
	list_display = ('company_name', 'lat', 'lon')


admin.site.register(Location, LocationAdmin)
