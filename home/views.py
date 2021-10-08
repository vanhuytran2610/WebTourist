from django.shortcuts import render
from django.http import HttpResponse
from centraltravel.models import Post_Central
from northtravel.models import Post_North
from southtravel.models import Post_South

# Create your views here.
def home_view(request):
    Data = {'Posts_North': Post_North.objects.all().order_by('-upload_to'),
            'Posts_Central': Post_Central.objects.all().order_by('-upload_to'),
            'Posts_South': Post_South.objects.all().order_by('-upload_to')}
    return render(request, 'pages/home.html', Data)

def information(request):
    return render(request, 'pages/information.html')


