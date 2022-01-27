from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect

from rmcsite.models import Gallery, Query

# Create your views here.
def home(request):
    events = Gallery.objects.all()
    print(events)
    return render(request,'base.html',{'events':events})

def cast(request):
    return render(request,'cast.html')

def query(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        query = request.POST['query']
        data = Query(name=name,email=email,subject=subject,query=query)
        data.save()
    return redirect(home)


    


