from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import xml_data #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import register #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import login_user #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import logout_user #sesuaikan dengan nama fungsi yang dibuat
from wishlist.views import show_wishlist_ajax
from wishlist.views import json_data, GetData


app_name = 'wishlist'


urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml_data, name='xml'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('json/', json_data, name='json_data'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('ajax/get', GetData.as_view(), name='get_data')
]