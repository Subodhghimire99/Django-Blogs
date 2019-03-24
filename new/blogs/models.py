from django.db import models
from django.urls import reverse

class new_post(models.Model):
	title = models.CharField(max_length=80,default="Not inserted")
	photo = models.FileField()
	desc = models.TextField()

	def get_absolute_url(self):
		return reverse('blogs:post_details',kwargs={"i":self.id})