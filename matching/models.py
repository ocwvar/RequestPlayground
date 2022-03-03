from django.db import models

# Create your models here.

class Match(models.Model):
    match_id = models.IntegerField(null=False)

class Score(models.Model):
    match_id = models.IntegerField(null=False)
    team_name_red = models.CharField(null=False, max_length=20)
    team_name_blue = models.CharField(null=False, max_length=20)
    score_red = models.IntegerField(null=False)
    score_blue = models.IntegerField(null=False)