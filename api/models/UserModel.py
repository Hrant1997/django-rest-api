from django.db import models
from .common import BaseModel

class User(BaseModel):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.name

