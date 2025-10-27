from django.shortcuts import render
from .models import Product

# Create your views here.
def new(request):
    return render(request,'home.html')

def userDetails(request):
    product=Product.objects.all()
    return render(request,'user.html',{'product':product})
def typesbutton(request):
    types=Product.objects.values_list('type',flat=True).distinct()
    return render(request,'types.html',{'types':types})
def getDetails(request, t):
    products=Product.objects.filter(type=t)
    return render(request,'user.html', {'products': products})




