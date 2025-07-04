from django.shortcuts import render,redirect
from .models import job
from django.core.paginator import Paginator
from  .forms import ApplyForm ,JobForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
def job_list (request):
    
    job_list = job.objects.all()
    paginator = Paginator(job_list, 3)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {'jobs':page_obj}
    return render(request,'job/job_list.html',context)

def job_details(request,slug):
    job_detail = job.objects.get(slug = slug)
    if request.method=='POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
           myform = form.save(commit=False)
           myform.job = job_detail
           myform.save()
    else:
        form = ApplyForm()
    context = {'jobs':job_detail, 'form' :  form}
    return render(request,'job/job_details.html',context)

@login_required
def add_job(request):
    if request.method =='POST':
        form = JobForm(request.POST , request.FILES)
      # if form.is_valid():
        myform = form.save(commit=False)
        myform.owner = request.user
        myform.save() 
        return redirect(reverse('jobs:job_list'))

    else:
        form = JobForm()
    return render(request,'job/add_job.html',{'form':form})
# Create your views here.
