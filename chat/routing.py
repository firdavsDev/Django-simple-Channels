import django


from django.urls import path, re_path

from . import consumers

websocket_urlpatterns = [
    path('ws/socket-server/', consumers.ChatCustomer.as_asgi()),
]