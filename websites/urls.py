from django.urls import path
from .views import home_page_view, add_record_view

urlpatterns = [
    path("",home_page_view, name='home'),
    path("add_job", add_record_view, name='add_record')
]