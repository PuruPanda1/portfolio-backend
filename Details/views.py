from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializer import *
from django.db.models.functions import Cast
from django.db.models import FloatField

class HeroDetailsView(APIView):
    def get(self, request):
        hero = HeroDetails.objects.latest('id')
        serializer = HeroDetailsSerializer(hero, many=False)
        return Response(serializer.data)


class EducationView(APIView):
    def get(self, request):
        education = Education.objects.all().order_by('-id')
        serializer = EducationSerializer(education, many=True)
        return Response(serializer.data)
    
class ExperienceView(APIView):
    def get(self, request):
        experience = Experience.objects.all().order_by('-id')
        serializer = ExperienceSerializer(experience, many=True)
        return Response(serializer.data)
    
class SkillView(APIView):
    def get(self, request):
        skill = Skill.objects.all().order_by('percentage')
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)
    
class ProjectView(APIView):
    def get(self, request):
        project = Project.objects.all().order_by('-id')
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)
    
class PortfolioView(APIView):
    def get(self, request):
        hero = HeroDetails.objects.latest('id')
        hero_serializer = HeroDetailsSerializer(hero, many=False)

        education = Education.objects.all().order_by('-id')
        education_serializer = EducationSerializer(education, many=True)

        experience = Experience.objects.all().order_by('-id')
        experience_serializer = ExperienceSerializer(experience, many=True)

        skill = Skill.objects.annotate(
            percentage_float=Cast('percentage', FloatField())
        ).order_by('-percentage_float')
        skill_serializer = SkillSerializer(skill, many=True)

        projects = Project.objects.prefetch_related('photos').all().order_by('-id')
        project_serializer = ProjectSerializer(projects, many=True, context={'request': request})

        # project = Project.objects.all().order_by('-id')
        # project_serializer = ProjectSerializer(project, many=True)

        data = {
            'hero': hero_serializer.data,
            'education': education_serializer.data,
            'experience': experience_serializer.data,
            'skill': skill_serializer.data,
            'project': project_serializer.data,
        }

        return Response(data)