from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import json


class ListUsers(APIView):
    def get(self, request, format=None):
        usernames = open('/home/kachigos/parsing/habr_app/all_categories_dict.json', 'r')
        return Response(json.load(usernames))


