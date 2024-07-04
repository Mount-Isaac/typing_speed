from django.urls import path, re_path

from user_management.views import (
    page404
)

from .views import (
    typing_speed_view
)

urlpatterns = [
    path('typing-speed', typing_speed_view, name='typing-speed'),
]  

urlpatterns += [
    re_path(r'^(?!auth|login).*$', page404, name='page404')
]

