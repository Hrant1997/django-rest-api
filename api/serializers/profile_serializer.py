from rest_framework import serializers

from api.models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('name', 'alias')
        
    def create(self, validated_data):
        return Profile.objects.create(**validated_data)
