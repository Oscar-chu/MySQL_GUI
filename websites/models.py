from django.db import models


# turning the database in db.py into a model
class JobSearchRecord(models.Model):
    application_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=250, blank=True, null=True)
    company_name = models.CharField(max_length=150, blank=True, null=True)
    application_date = models.DateField(blank=True, null=True)
    interview_status = models.IntegerField(blank=True, null=True)
    application_result = models.IntegerField(blank=True, null=True)
    job_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "job_search_record"
