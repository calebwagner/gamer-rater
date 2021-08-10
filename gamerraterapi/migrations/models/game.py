from django.db import models
from django.db.models.fields import DateField


class Game(models.Model):
    """Game Model
    """
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=150)
    # player = models.ForeignKey("Player", on_delete=models.CASCADE)
    year_released = DateField()
    number_of_players = models.IntegerField()
    game_duration = models.IntegerField()
    categories = models.ManyToManyField("Category", through="JoinCategory", related_name="category")
    recommended_age = models.IntegerField()
    creator = models.CharField(max_length=100)