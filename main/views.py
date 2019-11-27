from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Jumia,Perfecto
#from .forms import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator

def home(request):   
        data = Perfecto.objects.all()

        # paginator = Paginator(data, 5)

        # page = request.GET.get('page')
 
        # data = paginator.get_page(page)

        return render(request,'index.html',{'data':data})
    
def get_more_tables(request):
    increment = int(request.GET['append_increment'])
    increment_to = increment + 10
    data = Perfecto.objects.order_by('-id')[increment:increment_to]
    return render(request, 'get_more_tables.html', {'data': data})