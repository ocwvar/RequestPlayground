from dataclasses import field
from rest_framework import serializers
from .models import Match, Score

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = ('match_id')


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ('match_id', 'team_name_red', 'team_name_blue', 'score_red', 'score_blue')