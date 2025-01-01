from django.contrib import admin

# import the JobSearchRecord into the admin site
from .models import JobSearchRecord

admin.site.register(JobSearchRecord)
