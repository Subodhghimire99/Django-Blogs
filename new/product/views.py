from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Detail
from .forms import register_form
from django import forms

'''
Below is raw form but not a model form  ----------------------
		def input_view(request,*args,**kwargs):
			form_obj=DetailForm()
			if request.method == "POST":
				form_obj=DetailForm(request.POST)
				if form_obj.is_valid():
					Detail.objects.create(**form_obj.cleaned_data)
			context={
				"f":form_obj,
			}
			return render(request,"input.html",context)

          ------------------------------
dynamic display_view

		def dymnamic_look(request, i):
			obj=Detail.objects.get(id=i)
			context={
				"a":obj
			}
			return render(request,"display.html",context)
'''

def base_view(request,*args, **kwargs):
	return render(request,"base.html",{}) 


def input_view(request,*args,**kwargs):
	register_obj=register_form(request.POST or None) #initial= initial_data for showing in view
	if register_obj.is_valid():
			register_obj.save()
			return redirect("/")
	context={
		"f":register_obj,
	}				
	return render(request,"product/input.html",context)	


def dynamic_input_view(request,h):
	grab=get_object_or_404(Detail,id=h)
	register_obj=register_form(request.POST or None,instance=grab) #initial= initial_data(where initial_data is a dictonary) for showing in view
	if register_obj.is_valid():
			register_obj.save()
			return redirect("/")
	context={
		"f":register_obj,
	}				
	return render(request,"product/input.html",context)


	
def display_view(request,*args,**kwargs):
	model_obj=Detail.objects.all()
	disp={
		"a":model_obj,
	}
	return render(request,"product/all.html",disp)

def dymnamic_look(request, i):
	obj=get_object_or_404(Detail, id=i)
	# obj=Detail.objects.get(id=i)
	'''
	 try:	
		obj=Detail.objects.get(id=i)
	except Detail.DoesNotExist:
		raise Http404
	'''
	if request.method == "POST":
		obj.delete()
		return redirect("/product/display/")
	context={
		"a":obj,
	}
	return render(request,"product/display.html",context)

# def Detail_list(request,*args,**kwargs):
# 	queryset=Detail.objects.all()
# 	instance=Detail()
# 	context={
# 		"a":queryset,
# 		"b":instance
# 	}
# 	return render(request,"all.html",context)



def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			print(UserCreationForm(request.POST))
			form.save()
			form = UserCreationForm()
			return redirect('/')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form':form})

def registered(request):
	count = User.objects.all()
	return render(request, 'users.html', {'count':count})
