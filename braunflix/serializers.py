from braunflix.models import Program
from rest_framework import serializers


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ['title', 'kind', 'release_date', 'likes']