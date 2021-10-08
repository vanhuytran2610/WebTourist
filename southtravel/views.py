from django.shortcuts import render
from .models import Post_South

# Create your views here.
def list(request):
    Data = {'Posts_South': Post_South.objects.all().order_by('-upload_to')}
    return render(request, 'southtravel/south.html', Data)

def post(request, id):
    post = Post_South.objects.get(id = id)
    return render(request, 'southtravel/postSouth.html', {'postSouth': post})