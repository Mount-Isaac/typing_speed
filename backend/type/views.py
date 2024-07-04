from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Create your views here.
class TypingSpeedAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        return Response(status=HTTP_200_OK)


typing_speed_view = TypingSpeedAPIView.as_view()