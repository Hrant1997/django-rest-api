from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework import permissions


class ProfileDetailApiView(APIView):
    # add permission to check if user is authenticated
    permission_classes = [permissions.IsAuthenticated]

    # 3. Retrieve
    def get(self, request, profile, *args, **kwargs):
        serializer = ProfileSerializer(profile)
        return Response({'profile':serializer.data}, status=status.HTTP_200_OK)

    # # 4. Update
    def put(self, request, profile, *args, **kwargs):
        return Response('{"todo":"TODO"}')
    # TODO
        # data = {
        #     'task': request.data.get('task'), 
        #     'completed': request.data.get('completed'), 
        #     'user': request.user.id
        # }
        # serializer = ProfileSerializer(instance = profile, data=data, partial = True)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # # 5. Delete
    def delete(self, request, profile, *args, **kwargs):
        profile.delete()
        return Response(
            {"res": "Profile deleted!"},
            status=status.HTTP_200_OK
        )