from rest_framework.views import  APIView
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import ProfileSerializer
from api.models import Profile


class ProfileViewSet(APIView):
    # queryset = Profile.objects.all().order_by('name')
    # serializer_class = ProfileSerializer
    def get(self, request, profile: Profile = None):
        if profile:
            return Response({
                'profile': ProfileSerializer(profile).data
            })

        profiels = Profile.objects.all()
        return Response({
            'profiles': ProfileSerializer(profiels, many = True).data, 
        })
        
    def post(self, request):
        serializer = ProfileSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        
        new_profile = serializer.create(serializer.validated_data)
        return Response({
            'profile': ProfileSerializer( new_profile ).data
        })
    
    
        
    # @action(detail=True, methods=['post'])
    # def set_password(self, request, pk=None):
    #     user = self.get_object()
    #     serializer = PasswordSerializer(data=request.data)
    #     if serializer.is_valid():
    #         user.set_password(serializer.validated_data['password'])
    #         user.save()
    #         return Response({'status': 'password set'})
    #     else:
    #         return Response(serializer.errors,
    #                         status=status.HTTP_400_BAD_REQUEST)