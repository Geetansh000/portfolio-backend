from django.db import models

# Create your models here.

class Project(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=255)
    description = models.JSONField()
    tech_skills = models.JSONField()
    strong_words = models.JSONField(null=True, blank=True)
    type = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    role = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    created_by = models.ForeignKey('auth.User', null=True, on_delete=models.DO_NOTHING, related_name='created_projects')
    updated_by = models.ForeignKey('auth.User', null=True, on_delete=models.DO_NOTHING, related_name='updated_projects')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    