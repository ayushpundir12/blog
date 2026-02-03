from django import forms
from blogs.models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        from blogs.models import Category
        model = Category
        fields = '__all__'
        