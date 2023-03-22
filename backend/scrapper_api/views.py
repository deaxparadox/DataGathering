from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


from scrapper.models import Data, Site
from . import serializers

class SiteListView(generics.ListAPIView):
    serializer_class = serializers.SiteSerializer
    queryset = Site.objects.all()

class SitePendingListView(generics.ListAPIView):
    serializer_class = serializers.SiteSerializer
    queryset = Site.pending.all()


class SiteDoneListView(generics.ListAPIView):
    serializer_class = serializers.SiteSerializer
    queryset = Site.done.all()

class SiteCreateView(generics.CreateAPIView):
    serializer_class = serializers.SiteCreateSerializer
    queryset = Site.objects.all()

   
class SiteUpdateView(generics.UpdateAPIView):
    serializer_class = serializers.SiteStatusUpdateSerializer
    queryset = Site.objects.all()
    lookup_field = "id"


class DataListView(generics.ListAPIView):
    serializer_class = serializers.DataSerializer
    queryset = Data.objects.all()


class GetPendingSite(generics.ListAPIView):
    serializer_class = serializers.GetPending
    
    def get_queryset(self):
        query = Site.pending.first()
        if query:
            # Set status to "ST", "Start"
            # Meaning site is being scrapped
            query.status = "ST"
            query.save()
            return [query]
        return []
    