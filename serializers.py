from rest_framework import serializers
from .models import *

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
      class Meta:
          model=Profile
          fields='__all__'