from rest_framework import serializers

from api.models.ProfileModel import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'alias')
        