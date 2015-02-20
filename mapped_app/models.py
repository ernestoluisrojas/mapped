from django.db import models


class Location(models.Model):
	company_name = models.CharField(max_length=128)
	lat = models.FloatField()
	lon = models.FloatField()

	def __unicode__(self):
		return self.company_name

