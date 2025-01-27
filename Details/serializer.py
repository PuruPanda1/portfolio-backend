from rest_framework import serializers
from .models import *
from django.conf import settings

class HeroDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroDetails
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_photos(self, obj):
        # Get the request from the context
        request = self.context.get('request')
        if request:
            base_url = request.build_absolute_uri('/')  # Get server base URL
        else:
            base_url = settings.MEDIA_URL  # Fallback to media URL

        # Prepend base URL to image paths
        return [f"{base_url}media/{photo.photo}" for photo in obj.photos.all()]

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'