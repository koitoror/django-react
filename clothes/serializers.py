from rest_framework import serializers
from .models import Clothe

class ClotheSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothe
        fields = ('name', 'age', 'clad_type', 'color', 'created_at', 'updated_at')
