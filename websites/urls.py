from django.urls import path
from .views import home_page_view, add_record_view, update_record_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("add_job", add_record_view, name="add_record"),
    path(
        "update_record/id=<int:target_job_id>", update_record_view, name="update_record"
    ),
]
