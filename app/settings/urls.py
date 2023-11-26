from django.contrib import admin
from django.urls import path

from currency.views import (
    rate_list,
    status_code,
    test_template,
    rate_create,
    rate_update,
    rate_delete,
    request_method,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', rate_list),
    path('rate/create/', rate_create),
    path('rate/update/<int:pk>/', rate_update),
    path('rate/delete/<int:pk>/', rate_delete),
    path('sc/', status_code),
    path('template/', test_template),
    path('rm/', request_method),
]
