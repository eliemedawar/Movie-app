from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateVideoForm, FindByIDForm
from .models import Video

def index(request):
    return render(request, 'index.html')

def add_video(request):
    if request.method == 'POST':
        form = CreateVideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = CreateVideoForm()
    videos = Video.objects.order_by('MovieTitle')
    return render(request, 'add_video.html', {'form': form, 'videos': videos})

def list_videos(request):
    videos = Video.objects.order_by('MovieTitle')
    return render(request, 'list_videos.html', {'videos': videos})

def edit_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        form = CreateVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('list_videos')
    else:
        form = CreateVideoForm(instance=video)
    return render(request, 'add_video.html', {'form': form, 'videos': []})

def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if request.method == 'POST':
        video.delete()
        return redirect('list_videos')
    return render(request, 'confirm_delete.html', {'video': video})

def report_video(request):
    found = None
    if request.method == 'POST':
        form = FindByIDForm(request.POST)
        if form.is_valid():
            MovieID = form.cleaned_data['MovieID']
            found = Video.objects.filter(MovieID=MovieID).first()
    else:
        form = FindByIDForm()
    return render(request, 'report_video.html', {'form': form, 'found': found})