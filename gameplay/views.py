from json import JSONDecoder
from typing import Dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from .models import GameMatch as Match
from .models import GameScore as Score
from RequestPlayground.base_response import *
import json


class GameMatchRequestHandler(APIView):


    # DELETE for "match" will remove match and it's score as well
    def delete(self, request, *args, **kwargs):
        search_match_id = self.request.GET.get("match_id", -1)
        result_objects = Score.objects.filter(match_id = search_match_id)
        if result_objects.count() > 0 :
           result_objects.delete()
        
        return give_success_response("done")


    # GET for "match" will return a list of matches
    def get(self, request, *args, **kwargs):
        records = []
        for record in Match.objects.all() :
            records.append(
                {
                    "match_id": record.match_id
                }
            )
        
        return give_success_response_with_object(records)


class GameScoreRequestHandler(APIView):

    # GET for "score" will return a match data with given "match_id"
    def get(self, request, *args, **kwargs):
        # find match
        search_match_id = self.request.GET.get("match_id", -1)
        if search_match_id == -1 :
            return give_error_response("can not find match_id")

        # find score
        result_object = Score.objects.filter(match_id = search_match_id)
        if result_object.count() <= 0:
            return give_error_response("no such match")
        
        return give_success_response_with_object({
            "match_id": result_object[0].match_id,
            "team_name_red": result_object[0].team_name_red,
            "team_name_blue": result_object[0].team_name_blue,
            "score_red": result_object[0].score_red,
            "score_blue": result_object[0].score_blue
        })

    
    # POST for "score" will add new score and match into DB
    def post(self, request, *args, **kwargs):
        request_json: Dict = json.loads(self.request.body)
        new_match_id: int = request_json.get("match_id")
        new_team_name_red: str = request_json.get("team_name_red")
        new_team_name_blue: str = request_json.get("team_name_blue")
        new_score_red: int = request_json.get("score_red")
        new_score_blue: int = request_json.get("score_blue")

        if new_match_id == None :
            return give_error_response("match_id must not be none")

        if Match.objects.filter(match_id = new_match_id).count() > 0 :
            return give_error_response("match_id already existed")
        
        new_match: Match = Match(match_id = new_match_id)
        new_score: Score = Score(
            match_id = new_match_id, 
            team_name_red = new_team_name_red, 
            team_name_blue = new_team_name_blue, 
            score_red = new_score_red,
            score_blue = new_score_blue
        )

        new_score.save()
        new_match.save()

        return give_success_response("saved")


        
    