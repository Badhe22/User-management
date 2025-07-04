from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import UserSerializer
from .permissions import IsAdminOrSelf

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminOrSelf]

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrSelf])
    def disable(self, request, pk=None):
        user = self.get_object()
        user.is_disabled = True
        user.save()
        return Response({"status": "disabled"})

    @action(detail=True, methods=["post"], permission_classes=[IsAdminOrSelf])
    def enable(self, request, pk=None):
        user = self.get_object()
        user.is_disabled = False
        user.save()
        return Response({"status": "enabled"})

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
        })
