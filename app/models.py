from django.db import models


class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	publication_date = models.DateField(auto_now=True)

	def __str__(self):
	    return self.title