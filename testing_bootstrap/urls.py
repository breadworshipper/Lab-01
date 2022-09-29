from django.urls import path
from testing_bootstrap.views import show_bootstrap_testing

app_name = 'example_app'

urlpatterns = [
    path('', show_bootstrap_testing, name='show_bootstrap_testing'),
]