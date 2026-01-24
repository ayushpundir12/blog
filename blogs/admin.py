from django.contrib import admin
from .models import Category
from .models import blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display=('title','author','status','is_featured','category')
    search_fields=('title','author','status','id','category__category_name',)
    list_editable = ('status','is_featured',)



admin.site.register(Category)
admin.site.register(blog,BlogAdmin)


