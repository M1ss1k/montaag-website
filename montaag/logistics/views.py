from django.shortcuts import render, redirect
from .models import LogisticsTariffs
from .forms import Order

def index(request):
    return render(request, "logistics/index.html")

def tariffs(request):
    return render(request, "logistics/prices.html", context={'tariffs': LogisticsTariffs.objects.all()})

def contact(request):
    return render(request, "logistics/contact.html")

def create_order(request):
    if request.method == 'POST':
        form = Order(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect(f'/')
        
    else: 
        form = Order()
    return render(request, 'logistics/order_form.html', context={'form':form})

# Create your views here.
