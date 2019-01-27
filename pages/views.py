from django.shortcuts import render
#from django.http import HttpResponse #only for html from here

def index(request):
    return render(request,'pages/index.html')
def about(request):
    return render(request,'pages/about.html')
