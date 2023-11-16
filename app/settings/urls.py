from django.contrib import admin
from django.urls import path

from currency.views import rate_list, status_code, test_template

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('sc/', status_code),
    path('template/', test_template)
]
