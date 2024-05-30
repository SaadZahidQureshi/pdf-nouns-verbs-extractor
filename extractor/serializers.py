from rest_framework import serializers
from .models import ExtractedData

class ExtractedDataSerializer(serializers.ModelSerializer):
    nouns = serializers.JSONField(required=False)
    verbs = serializers.JSONField(required=False)
    
    class Meta:
        model = ExtractedData
        fields = '__all__'

