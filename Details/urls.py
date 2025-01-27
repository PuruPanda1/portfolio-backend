from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('hero/', HeroDetailsView.as_view(), name='hero'),
    path('education/', EducationView.as_view(), name='education'),
    path('experience/', ExperienceView.as_view(), name='experience'),
    path('skill/', SkillView.as_view(), name='skill'),
    path('project/', ProjectView.as_view(), name='project'),
    path('portfolio/', PortfolioView.as_view(), name='portfolio'),
]

