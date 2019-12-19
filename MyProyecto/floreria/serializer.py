from rest_framework import serializers
from .models import Flores

class FlorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Flores
        fields = ['name','valor','descripcion','stock']