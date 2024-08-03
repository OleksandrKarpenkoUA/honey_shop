from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from main.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='goods')),
]

handler404 = page_not_found

if not settings.TESTING:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
