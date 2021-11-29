from rest_framework.generics import RetrieveAPIView, UpdateAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserProfile
from users.serializers import ProfileDetailSerializer, ProfileSerializer


class ProfileDetail(RetrieveAPIView):
    """Profile detail for un-!!-authentificated user"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = ProfileDetailSerializer


class ProfileDetailMe(APIView):
    """Profile detail for authentificated user"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        profile = get_object_or_404(UserProfile, user=request.user)
        serializer = ProfileDetailSerializer(profile, many=False)
        return Response(serializer.data)


class ProfileUpdate(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer


class ProfileCreate(CreateAPIView):
    """If user is authorized, profile there is no need to create"""
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
