from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib import admin


urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),
    # Include the health health's URLs with the namespace 'health'
    path('', include(('health.urls', 'health'), namespace='health')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
