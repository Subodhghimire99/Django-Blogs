from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django import forms
from .forms import new_blog_form
from .models import new_post

def blogs_home(request,*args,**kwargs):
	all=new_post.objects.all()
	context={
			"all_posts" : all,
		}
	return render(request,"blogs/blog_home.html",context)

def new_posts(request,*args,**kwargs):
	input_data = new_blog_form(request.POST or None )
	input_data = new_blog_form(request.POST or None, request.FILES or None)
	if input_data.is_valid():
		input_data.save()
		return redirect('/blogs/')
	context = {
			"form":input_data,
		}
	return render(request,'blogs/blog_content.html',context)

def post_detail(request,i):
	obj=get_object_or_404(new_post,id=i)
	context = {"a":obj,}
	if request.method == "POST":
		obj.delete()
		return redirect('/blogs/')
	return render(request,'blogs/blog_detail.html',context)
