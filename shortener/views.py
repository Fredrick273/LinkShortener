from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ShortenUrl
import random
import string
from django.contrib import messages

site = "http://127.0.0.1:8000/"

def createRandom():
    code = ""
    a = string.ascii_lowercase
    i=0
    while i < 6:
        code += (random.choice(a))
        i = i+1
    return code

# Create your views here.

def redirect(request,*args,**kwargs):
    print(kwargs)
    obj = ShortenUrl.objects.all()
    if ShortenUrl.objects.filter(code=kwargs['code']).exists():
        content = ShortenUrl.objects.get(code=kwargs['code'])
        print(content.link)
        return HttpResponseRedirect(content.link)
    else:
        messages.error(request,"Url not found")
        return render(request,'codes.html',{'Urls':obj,'site':site})

def create(request):
    obj = ShortenUrl.objects.all()
    link = request.POST.get('Link', None)
    name = request.POST.get('Name', None)
    check = True
    while check:
        code = createRandom()
        if not(ShortenUrl.objects.filter(code=code).exists()):
            check = False
    new = ShortenUrl.objects.create(name=name,link=link,code=code)
    new.save()
    messages.success(request, (f"Link is {site}re/{code}"))
    return render(request,'codes.html',{'Urls':obj,'site':site})


def codes(request):
    obj = ShortenUrl.objects.all()
    ShortenUrl.objects.filter(name="youtube").delete()
    return render(request,'codes.html',{'Urls':obj,'site':site})
