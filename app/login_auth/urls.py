from . import views
from django.urls import path

urlpatterns=[
    path('login/',views.login,name='login_view'),
]

