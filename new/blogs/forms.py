from django import forms
from .models import new_post



class new_blog_form(forms.ModelForm):
	class Meta:
		model = new_post
		fields = [
				"title",
				"photo",
				"desc",
			]