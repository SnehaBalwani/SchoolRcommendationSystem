from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# from django.conf.urls import *
admin.autodiscover()

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('sch.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
