from django.shortcuts import render
from datetime import datetime
# Create your views here.
def home(request):
    dataArray = {'date': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
    return render(request, 'pizza/home.html', dataArray)


def order(request):
    dataArray = {'date': datetime.now().strftime("%b %d, %Y %H:%M:%S")}
    return render(request, 'pizza/order.html', dataArray)