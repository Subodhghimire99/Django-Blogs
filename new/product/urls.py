from django.urls import path
from product.views import (
					base_view,
					input_view,
					display_view,
					dynamic_input_view,
					dymnamic_look,
					)

app_name ='product'
urlpatterns = [
    path('input/',input_view,name='info'),
    path('input/<int:h>/',dynamic_input_view,name='xtra'),
    path('display/',display_view,name='ok'),
    path('display/<int:i>/',dymnamic_look,name='new'),  
]