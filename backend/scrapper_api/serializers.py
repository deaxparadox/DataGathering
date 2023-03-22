from rest_framework import serializers

from scrapper.models import Site, Data

class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site 
        fields = ("url", "name", "status", "domain")
        
class SiteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site 
        fields = ("url", "name", "domain")

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ("text")

class GetPending(serializers.ModelSerializer):
    class Meta:
        model = Site 
        fields = ("url", )