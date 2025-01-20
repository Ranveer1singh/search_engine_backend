from rest_framework import serializers

class SearchQuerySerializer(serializers.Serializer):
    query = serializers.CharField(max_length = 200)
    filters = serializers.JSONField(required = False)