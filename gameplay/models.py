from django.db import models

# Create your models here.

class GameMatch(models.Model):
    match_id = models.IntegerField(null=False)


class GameScore(models.Model):
    match_id = models.IntegerField(null=False)
    team_name_red = models.CharField(null=False, max_length=20, default="team_1")
    team_name_blue = models.CharField(null=False, max_length=20, default="team_2")
    score_red = models.IntegerField(null=False)
    score_blue = models.IntegerField(null=False)