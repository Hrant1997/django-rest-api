from django.db import models
from .common import BaseModel

class Profile(BaseModel):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name