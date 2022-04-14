from symtable import Symbol
from django.http import JsonResponse
from django.shortcuts import render
from .models import Bhav
# Create your views here.
def index(request):
    return render(request,'index.html')

def stocks_det(request):
    data=request.GET['input'].upper()
    print(data)
    stocks_details=Bhav.objects.filter(symbol=data)
    print(stocks_details)
    if stocks_details.count()==0:
    	return render(request,'index.html')
    return render(request,'stocks.html',{'stocks_details':stocks_details})
