from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import player


# Create your views here.

class playerAPIView(APIView):

    def get(self, request):
        objs = player.objects.all()
        result = []
        for obj in objs:
            temp = {
                "id": obj.pid,
                "name": obj.name,
                "rank": obj.rank,
                "skill": obj.skill,
                "captain": obj.captain,
                "created": obj.created
            }
            result.append(temp)

        return Response(result, status=status.HTTP_200_OK)

    def post(self, request):
        name = request.data['name']
        rank = request.data['rank']
        skill = request.data['skill']
        captain = request.data['captain']

        obj = player.objects.create(name=name, rank=rank, skill=skill, captain=captain)
        return Response(f"{obj.name} created", status=status.HTTP_201_CREATED)

    def delete(self, request, id=id):
        obj = player.objects.get(pid=id)
        if obj:
            obj.delete()
            return Response({"Deleted": f"{obj.name}"})

    def put(self, request, id=id):
        obj = player.objects.get(pid=id)
        if obj:
            obj.name = request.data['name']
            obj.rank = request.data['rank']
            obj.skill = request.data['skill']
            obj.captain = request.data['captain']
            obj.save()
            return Response({"updated": f"{obj.name}"})
