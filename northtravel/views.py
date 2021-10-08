from django.shortcuts import render
from .models import Post_North


# Create your views here.
def list(request):
    Data = {'Posts_North': Post_North.objects.all().order_by('-upload_to')}
    return render(request, 'northtravel/north.html', Data)

def post(request, id):
    post = Post_North.objects.get(id = id)
    return render(request, 'northtravel/postNorth.html', {'postNorth': post})