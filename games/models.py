from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=150)
    genre = models.CharField(max_length=50)
    release_year = models.IntegerField()
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} ({self.genre})"
    