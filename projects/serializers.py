from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

def create(self, validated_data):
    if 'title' in validated_data and not validated_data.get('slug'):
        import re
        title = validated_data['title'].lower()
        slug = re.sub(r'\W+', '_', title)
        slug = re.sub(r'_+', '_', slug).strip('_')
        validated_data['slug'] = slug
    return super().create(validated_data)