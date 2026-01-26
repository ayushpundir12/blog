from .models import Category
from assignment.models import SocialLink

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def social_links(request):
    sociallink=SocialLink.objects.all()
    return dict(sociallink=sociallink)