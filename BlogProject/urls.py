
from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static 
from Blog import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('users/', include("django.contrib.auth.urls")),
    path('users/', include("users.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

