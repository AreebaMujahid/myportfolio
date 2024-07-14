

# Create your views here.
# views.py

from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import VideoForm
from .models import Video

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully uploaded")  # Redirect to a success page or another view
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def success(request):
    videos = Video.objects.all()  # Fetch all videos from the database
    return render(request, 'success.html', {'videos': videos})
