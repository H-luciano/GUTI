from django.shortcuts import render


def home(request):
    return render(request,'home/guti_home.html',{})
