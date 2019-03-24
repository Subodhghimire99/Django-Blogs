from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from product.views import base_view

urlpatterns = [
        path('product/',include('product.urls')),
        path('blogs/',include('blogs.urls')),
        path('',base_view,name='home'),
        path('admin/', admin.site.urls),
    ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)