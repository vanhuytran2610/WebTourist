from django.shortcuts import render
from .models import Post_Central

# Create your views here.
def list(request):
    Data = Post_Central.objects.all()
    return render(request, 'centraltravel/central.html', {'Posts_Central': Data})

def post(request, id):
    post = Post_Central.objects.get(id = id)
    return render(request, 'centraltravel/postCentral.html', {'postCentral': post})