from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from currency.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('account.urls')),

    path('currency/', include('currency.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', IndexView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # url /media/... -> file system /media/
