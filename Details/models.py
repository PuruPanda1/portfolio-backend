from django.db import models
import os

# function to create folder for each project
def project_photo_upload_to(instance, filename):
    project_folder = f"projects/{instance.project.title.replace(' ', '_')}"
    return os.path.join(project_folder, filename)

class HeroDetails(models.Model):
    image_address = models.CharField(max_length=1024)
    resume_link = models.CharField(max_length=1024)
    typewriter_text = models.JSONField(default=list)
    hero_bio = models.TextField()
    about_me = models.TextField()
    github_link = models.CharField(max_length=1024)
    linkedin_link = models.CharField(max_length=1024)
    instagram_link = models.CharField(max_length=1024)

    def __str__(self):
        return self.resume_link

class Education(models.Model):
    title = models.CharField(max_length=256)
    school = models.CharField(max_length=256)
    duration = models.CharField(max_length=100)

    def __str__(self):
        return self.title + ' at ' + self.school
    
class Experience(models.Model):
    title = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    duration = models.CharField(max_length=100)
    description = models.JSONField(default=list)


    def __str__(self):
        return self.title + ' at ' + self.company
    
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    animation = models.CharField(max_length=1024, default='')
    objectives = models.JSONField(default=list)
    tech_stack = models.JSONField(default=list)
    orientation = models.CharField(max_length=100, default='landscape')

    def __str__(self):
        return self.title

class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, related_name="photos", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=project_photo_upload_to)

    def __str__(self):
        return f"Photo for {self.project.title}"    

class Skill(models.Model):
    title = models.CharField(max_length=256)
    percentage = models.CharField(max_length=100)
    photo_address = models.CharField(max_length=1024, default='')
    isLeft = models.BooleanField(default=True)

    def __str__(self):
        return self.title + ' - ' + self.percentage