from django.shortcuts import render

# Create your views here.
def home(request):
    #products = Product.objects.all()
    return render(request, 'farmerapp/home.html')#, {'products': products})


def login(request):
    return render(request,'farmerapp/login.html')