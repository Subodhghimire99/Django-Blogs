from django.db import models
from django.urls import reverse
import datetime


class Detail(models.Model):
	Name=models.CharField(max_length=100)
	Rollno=models.CharField(max_length=7)
	Country=models.CharField(max_length=40)
	Email=models.EmailField(max_length=70)
	Description=models.CharField(max_length=200)
	sn=models.IntegerField(default=1)

	def get_absolute_url(self):
		return reverse("product:new", kwargs={"i": self.id})
		# return f"/display/{self.id}/"