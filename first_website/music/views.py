"""from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Album, Song
from django.http import Http404

# Create your views here.

def index(request):
    one approach:

    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse(html)

    below is a better approach:
    
    anoyher approach:

    all_albums = Album.objects.all()
    # context = {'all_albums' : all_albums}
    return render(request, 'music/index.html', {'all_albums' : all_albums})

def detail(request, album_id):
    one approach: 
    try:
        all_albums = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Sorry Album Not Found")
    return render(request, 'music/detail.html', {'albums' : all_albums})
    'music/detail.html' is the template

    below is a better approach:
    
    another approach:
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'albums' : album})

def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'albums' : album,
            'error_message' : 'You did not select a valid song',
        })
    else:
        selected_song.is_fav = True
        selected_song.save()
        return render(request, 'music/detail.html', {'albums' : album})
"""

# Gerenic View

from django.views import generic
from .models import Album
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()
    

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']

    

