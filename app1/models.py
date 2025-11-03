from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Video(models.Model):
    MovieID = models.PositiveIntegerField(primary_key=True)
    MovieTitle = models.CharField(max_length=200)
    Actor1Name = models.CharField(max_length=120)
    Actor2Name = models.CharField(max_length=120)
    DirectorName = models.CharField(max_length=120)
    MovieGenre = models.CharField(max_length=30)
    ReleaseYear = models.PositiveIntegerField(
        validators=[MinValueValidator(1888), MaxValueValidator(2100)]
    )

    def __str__(self):
        return f"{self.MovieTitle} ({self.ReleaseYear})"