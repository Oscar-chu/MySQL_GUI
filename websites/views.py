from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import JobSearchRecord
from django.core.paginator import Paginator
from .forms import Addform

def home_page_view(request):
    record = JobSearchRecord.objects.all().order_by('-application_id')
    paginator = Paginator(record,5)
    page_number = request.GET.get('page')
    record = paginator.get_page(page_number)

    context = {
        'record':record
    }
    return render(request,'home.html',context)


def add_record_view(request):
    form = Addform(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            add_record = form.save()
            return redirect('home')
    return render(request,'add_record.html',{'form':form})