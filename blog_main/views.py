from django.shortcuts import render
from blogs.models import Category,blog


def home(request):
    categories= Category.objects.all()
    featured_blogs= blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts= blog.objects.filter(status='Published',is_featured=False).order_by('-created_at')

    contex={'categories': categories, 
            'featured_blogs': featured_blogs,
             'posts': posts}
    return render(request,'home.html',contex)