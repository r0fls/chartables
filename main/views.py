from django.shortcuts import render
from models import Test

def home(request):
    #t = Test.objects.get(pk=1)
    t = Test.chart()
    return render(request, "home.html", context={'t':t})

# Create your views here.
