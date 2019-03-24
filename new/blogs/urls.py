from django.urls import path
from .views import (
		blogs_home,
		new_posts,
		post_detail,
	)



app_name='blogs'
urlpatterns=[
		path('',blogs_home,name='blogs_home'),
		path('upload/',new_posts,name="new_posts"),
		path('detail/<int:i>/',post_detail,name='post_details')
	]