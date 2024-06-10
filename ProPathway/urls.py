from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('internship/',include('internship.urls')),
    path('api/', include('api.urls')),
    path('discussions/', include('discussions.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)