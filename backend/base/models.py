import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    Custom user model 
    """
    name = models.CharField(max_length=100)
    organisation = models.CharField(max_length=100)
    
    def get_all_jobs(self):
        """ Returns all the jobs posted by this user

        Returns:
            [QuerySet]: jobs with foreign connection to this user
        """
        return self.job_set.all()

class Job(models.Model):
    job_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    applicant_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    questions = models.JSONField(blank=True,null=True)

    def __str__(self) -> str:
        return self.title