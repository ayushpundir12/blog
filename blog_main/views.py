from django.shortcuts import render
from blogs.models import Category,blog
from assignment.models import About


def home(request):
    categories= Category.objects.all()
    featured_blogs= blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts= blog.objects.filter(status='Published',is_featured=False).order_by('-created_at')
    

    try:
        about=About.objects.get()
    except :
        about=None


    contex={'categories': categories, 
            'featured_blogs': featured_blogs,
             'posts': posts,
             'about': about,}
    return render(request,'home.html',contex)