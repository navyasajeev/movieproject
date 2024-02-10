from django.shortcuts import render
from movieapp.models import Movie
# Create your views here.

from movieapp.forms import Bookform
def home(request):
    k = Movie.objects.all()
    return render(request, 'home.html', {'m': k})

def add(request):
    if(request.method=="POST"):
        n=request.POST['n']
        d = request.POST['d']
        y = request.POST['y']
        i = request.FILES['i']
        m=Movie.objects.create(name=n,desc=d,year=y,image=i)
        m.save()
        return home(request)
    return render(request,'add.html')

def details(request,p):

        m = Movie.objects.get(id=p)
        return render(request, 'view.html', {'m': m})

def moviedelete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()
    return home(request)

def edit(request,p):
    b = Movie.objects.get(id=p)

    if (request.method == "POST"):
        form = Bookform(request.POST, request.FILES, instance=b)
        if form.is_valid():
            form.save()
        return home(request)

    form = Bookform(instance=b)
    return render(request, 'update.html', {'form': form})
