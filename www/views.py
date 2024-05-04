from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from datetime import date
from . import serializers, models


class MenstrualStatusDayAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, year, month, day):
        current_user = request.user
        current_date = date(year, month, day)

        objects_for_day = models.MenstrualDayStatus.objects.filter(user_id=current_user.id, date=current_date)
        serializer = serializers.MenstrualDayStatusSerializer(objects_for_day, many=True)
        if objects_for_day.exists():
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MenstrualStatusMonthAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, year, month):
        current_user = request.user
        objects_for_month = models.MenstrualDayStatus.objects.filter(user_id=current_user.id, date__year=year,
                                                                     date__month=month)
        serializer = serializers.MenstrualDayStatusSerializer(objects_for_month, many=True)
        if objects_for_month.exists():
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MenstrualStatusYearAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, year):
        current_user = request.user
        objects_for_year = models.MenstrualDayStatus.objects.filter(user_id=current_user.id, date__year=year)
        serializer = serializers.MenstrualDayStatusSerializer(objects_for_year, many=True)
        if objects_for_year.exists():
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MarkMenstrualDayStatus(APIView):
    @staticmethod
    def put(request, year, month, day):
        current_user = request.user
        date_to_mark = date(year, month, day)
        menstrual_day = models.MenstrualDayStatus.objects.filter(user_id=current_user.id, date=date_to_mark)
        serializer = serializers.MenstrualDayStatusSerializer(menstrual_day, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SymptomListAPIView(generics.GenericAPIView):
    queryset = models.Symptom.objects.all()
    serializer_class = serializers.SymptomListSerializer

    def get(self, request):
        current_user = request.user
        user_symptoms = models.Symptom.objects.filter(user_id=current_user.id)
        serializer = self.get_serializer(user_symptoms, many=True)
        return Response(serializer.data)

    def put(self, request):
        current_user = request.user
        symptom_data = request.data.get('symptoms', [])
        models.Symptom.objects.filter(id__in=symptom_data, user_id=current_user.id).update(is_active=True)
        models.Symptom.objects.exclude(id__in=symptom_data, user_id=current_user.id).update(is_active=False)
        return Response(self.serializer_class.data, status=204)
