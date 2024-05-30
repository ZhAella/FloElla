from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from . import serializers
from .serializers import UserSerializer, CustomUserCreateSerializer, UserUpdateSerializer


class JwtPairAPIView(TokenObtainPairView):
    serializer_class = serializers.JwtTokenSerializer


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        serializer = CustomUserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request):
        user = request.user
        data = request.data
        if any(field in data for field in ['username', 'email']):
            password = data.get('password', '')
            if not user.check_password(password):
                return Response({'error': 'Password is incorrect.'},
                                status=status.HTTP_400_BAD_REQUEST)
        serializer = UserUpdateSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            serializer_to_show = UserSerializer(user)
            return Response(serializer_to_show.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
