from django.urls import path

from .views import (
    page404
)

urlpatterns = [
    path('page404', page404, name='page404')
]