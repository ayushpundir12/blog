from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import blog,Category

# Create your views here.



def category_blogs(request, category_id):
    # Fetch posts for the specified category
    posts=blog.objects.filter(category=category_id, status='Published')
    # try:
    #     category =Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, pk=category_id)
    context={'posts':posts, 'category':category}
    return render(request, 'posts_by_category.html', context)
    return HttpResponse(posts)