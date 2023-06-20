from rest_framework import serializers
from app.models import *

class Bankserializers(serializers.ModelSerializer):
    class Meta:
        model=Bank
        fields='__all__'

class Branchserializers(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields='__all__'