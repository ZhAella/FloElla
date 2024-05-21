from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from . models import MenstrualDayStatus
from .serializers import MenstrualDayStatusRequestSerializer, MenstrualDayStatusResponseSerializer


class MenstrualDayStatusAPIView(APIView):
    pagination_class = PageNumberPagination
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None):
        if pk is not None:
            menstrual_status = get_object_or_404(MenstrualDayStatus, pk=pk)
            serializer = MenstrualDayStatusResponseSerializer(menstrual_status)
            return Response(serializer.data)

        paginator = self.pagination_class()
        statuses = MenstrualDayStatus.objects.filter(user_id=request.user).order_by('-start_data')
        result_page = paginator.paginate_queryset(statuses, request)
        serializer = MenstrualDayStatusResponseSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    @staticmethod
    def post(request):
        serializer = MenstrualDayStatusRequestSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            response_serializer = MenstrualDayStatusResponseSerializer(instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def put(request, pk):
        menstrual_status = get_object_or_404(MenstrualDayStatus, pk=pk)
        serializer = MenstrualDayStatusRequestSerializer(menstrual_status, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request, pk):
        menstrual_status = get_object_or_404(MenstrualDayStatus, pk=pk)
        menstrual_status.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



