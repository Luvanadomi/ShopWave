from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('items/',include('item.urls')),
    path('inbox/',include('inbox.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
