from django.shortcuts import render
from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class LikeHandleView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        like = cache.get(f"like:{id}")
        if not like:
            like = 0
        return Response({"like": like})

    def post(self, request, id):
        like = cache.get(f"like:{id}")
        if not like:
            like = 0
        cache.set(f"like:{id}", like+1)
        return Response({"success": "true"})
