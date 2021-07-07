from django.shortcuts import render
from django.http import HttpResponse
from .forms import Myform
from.models import Mysee

# Create your views here.
def home_page(request):
    if request.method == 'POST':
        data = Myform(request.POST)
        if data.is_valid():
            data.save()
        data = Myform()
        return render(request, 'home.html', {'data':data})
    else:
        data = Myform()
        return render(request, 'home.html', {'data':data})

