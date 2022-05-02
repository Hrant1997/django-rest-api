from rest_framework.views import  APIView
from rest_framework.decorators import action
from .common import ApiResponce
from api.serializers import ProfileSerializer
from api.models import Profile


class ProfileViewSet(APIView):
    def get(self, request):
        profiels = Profile.objects.all()
        return ApiResponce( ProfileSerializer(profiels, many = True) )
        
    def post(self, request):
        serializer = ProfileSerializer(data = request.data )
        serializer.is_valid(raise_exception=True)
        
        new_profile = serializer.create(serializer.validated_data)
        return ApiResponce( ProfileSerializer( new_profile ) )