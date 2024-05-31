from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

def gallery_view(request):
    # Your code here
    return render(request, 'gallery_view.html')