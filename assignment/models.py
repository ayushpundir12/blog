from django.db import models

# Create your models here.

class About(models.Model):

    about_heading=models.CharField(max_length=200)
    about_content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='About'

    def __str__(self):
        return self.about_heading
    

class SocialLink(models.Model):
    platform_name=models.CharField(max_length=100)
    profile_url=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='SocialLink'

    def __str__(self):
        return self.platform_name
