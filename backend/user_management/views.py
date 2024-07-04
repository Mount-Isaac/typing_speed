from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

# Create your views here.
class Page404APIView(APIView):
    def post(self, *args, **kwargs):
        return Response(status=HTTP_404_NOT_FOUND)

    def get(self, *args, **kwargs):
        return Response(status=HTTP_404_NOT_FOUND)

page404 = Page404APIView.as_view()