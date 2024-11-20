from django.shortcuts import render, redirect
from .models import Mahsulot, Sotuv
from .forms import SaleForm

def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sale_list')
    else:
        form = SaleForm()
    return render(request, 'sales/create_sale.html', {'form': form})

def product_list(request):
    products = Mahsulot.objects.all()
    return render(request, 'sales/product_list.html', {'products': products})

def sale_list(request):
    sales = Sotuv.objects.all()
    return render(request, 'sales/sales_list.html', {'sales': sales})

def index(request):
    return render(request,"home.html")