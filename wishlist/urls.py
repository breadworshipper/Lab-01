from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import xml_data #sesuaikan dengan nama fungsi yang dibuat

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml_data, name='xml_data'),
]