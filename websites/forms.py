from django import forms
from .models import JobSearchRecord


# form for adding new job application
class Addform(forms.ModelForm):
    job_title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Job Title", "class": "form-control"}
        ),
        label="",
    )
    company_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Company name", "class": "form-control"}
        ),
        label="",
    )
    application_date = forms.DateField(
        required=True,
        widget=forms.widgets.DateInput(
            attrs={"placeholder": "Date of application", "class": "form-control"}
        ),
        label="",
    )

    class Meta:
        model = JobSearchRecord
        exclude = (
            "interview_status",
            "application_result",
            "job_description",
        )  # omit these columns in the form


# create the form of updating a record
class Updateform(forms.ModelForm):
    class Meta:
        model = JobSearchRecord
        fields = ["interview_status", "application_result"]
