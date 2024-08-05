from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import page_not_found
from app import settings


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='goods')),
]

handler404 = page_not_found

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    
