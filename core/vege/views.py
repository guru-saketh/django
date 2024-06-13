from django.shortcuts import render
from .models import *

# Create your views here.
def receipes(request):
  if request.method =='POST':
    data =request.POST
    receipe_name =data.get('receipe_name')
    print(receipe_name)


  return render(request,'base.html')