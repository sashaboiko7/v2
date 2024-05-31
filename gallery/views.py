from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Image, Category

def gallery_view(request):
    categories = Category.objects.all()
    return render(request, 'gallery.html', { 'categories': categories })

def image_detail(request):
    # Your code here
    return render(request, 'image_detail.html')