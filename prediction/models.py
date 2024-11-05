from django.db import models
from profiles.models import UserProfile

class PredictionData(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    input_data = models.TextField()
    result = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction for {self.user.user.username} on {self.created_at}"
