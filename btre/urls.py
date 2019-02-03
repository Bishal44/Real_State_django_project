
from django.contrib import admin
from django.urls import path,include

#for media file
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('pages.urls')),
    path('listing/',include('listings.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# +static is for image to show