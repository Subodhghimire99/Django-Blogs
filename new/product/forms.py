from django import forms
from .models import Detail


class register_form(forms.ModelForm):
	Description=forms.CharField(widget=forms.Textarea(
			attrs={
				"rows":14,
				"columns":50,
			}
		)
	)
	Name=forms.TextInput(
			attrs={
				"placeholder":"Your Full Name",
			}
		)
	Email=forms.TextInput(
			attrs={
				"placeholder":"Must be a gmail1"
			}
		)
	class Meta:
		model=Detail
		fields=[
			'Name',
			'Rollno',
			'Country',
			'Email',
			'Description'
		]
	def clean_Country(self, *args, **kwargs):
		Country = self.cleaned_data.get("Country")
		if "Nepal" not in Country:
			raise forms.ValidationError("Only Allowed For Nepal")
		else:
			return Country
	def clean_Email(self, *args, **kwargs):
		Email = self.cleaned_data.get("Email")
		if not Email.endswith("gmail.com"):
			raise forms.ValidationError("Not a valid Email")
		else:
			return Email