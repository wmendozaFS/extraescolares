# actividad/models.py
from django.db import models
from django.contrib.auth.models import User
from core.models import 

class Actividad(models.Model):
    monitor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='actividades')
    actividad = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='actividades')
    plazas_max = models.PositiveIntegerField(null=False)
    description = models.CharField(null=False, max_length=100)
    completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} ({self.user.username})"