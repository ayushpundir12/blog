from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import blog,Category,Comment

from django.db.models import Q

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

def blogs(request, slug):
    single_blog = get_object_or_404(blog, slug=slug, status='Published')
    if request.method == 'POST':
        comment=Comment()
        comment.User=request.user
        comment.blog=single_blog
        comment.comment=request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    #comments
    comments=Comment.objects.filter(blog=single_blog).order_by('-created_at')
    comment_count=comments.count()
    context={'single_blog':single_blog, 'comments':comments,'comment_count':comment_count}
    return render(request, 'blogs.html', context)



def search(request):
    keyword=request.GET.get('keyword')

    blogs=blog.objects.filter(
        Q(title__icontains=keyword)
        |Q(short_description__icontains=keyword)
        |Q(blog_body__icontains=keyword),
        status='Published'
    )
    context={'blogs':blogs,
             'keyword':keyword}


    return render(request, 'search.html',context)