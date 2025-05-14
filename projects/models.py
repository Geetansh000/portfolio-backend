from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=250, unique=True)
    title = models.CharField(max_length=250)
    short_description = models.TextField()
    description = models.JSONField()
    tech_skills = models.JSONField()
    strong_words = models.JSONField()
    type= models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    role = models.CharField(max_length=250)
    icon = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
