from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import date
from users.models import GirlUser
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


class MenstrualStatusWeekAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, year=None, week=None):
        current_user = request.user
        current_date = timezone.now()

        if not all([year, week]):
            year = current_date.year
            week = current_date.isocalendar()[1]

        start_date = timezone.datetime.strptime(f"{year}-{week}-1", "%Y-%W-%w").date()
        end_date = start_date + timezone.timedelta(days=6)

        objects_for_week = models.MenstrualDayStatus.objects.filter(
            user_id=current_user.id,
            date__range=[start_date, end_date]
        )

        serializer = serializers.MenstrualDayStatusSerializer(objects_for_week, many=True)

        if objects_for_week.exists():
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class MenstrualStatusMonthAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, year, month):
        current_user = request.user
        objects_for_month = models.MenstrualDayStatus.objects.filter(
            user_id=current_user.id,
            date__year=year,
            date__month=month
        )
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


class MarkMenstrualStartDayStatus(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, year, month, day):
        user = get_object_or_404(GirlUser, id=request.user.id)
        date_to_mark = date(year, month, day)
        if user is not None:
            user.start_date = date_to_mark
            user.end_date = None
            user.save()

        menstrual_day, created = models.MenstrualDayStatus.objects.get_or_create(user_id=user, date=date_to_mark)
        if not created:
            menstrual_day.save()

        menstrual_day.name = "Menstrual day"
        menstrual_day.save()

        serializer = serializers.MenstrualDayStatusSerializer(menstrual_day, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkMenstrualDayStatus(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, year, month, day):
        user = get_object_or_404(GirlUser, id=request.user.id)
        date_to_mark = date(year, month, day)

        menstrual_day, created = models.MenstrualDayStatus.objects.get_or_create(user_id=user, date=date_to_mark)
        if not created:
            menstrual_day.save()

        menstrual_day.name = "Menstrual day"
        menstrual_day.save()

        serializer = serializers.MenstrualDayStatusSerializer(menstrual_day, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkMenstrualEndDayStatus(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def put(request, year, month, day):
        user = get_object_or_404(GirlUser, id=request.user.id)
        date_to_mark = date(year, month, day)
        if user is not None:
            user.end_date = date_to_mark
            user.save()

        menstrual_day, created = models.MenstrualDayStatus.objects.get_or_create(user_id=user, date=date_to_mark)
        if not created:
            menstrual_day.save()

        menstrual_day.name = "Menstrual day"
        menstrual_day.save()

        serializer = serializers.MenstrualDayStatusSerializer(menstrual_day, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SymptomAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, year, month, day):
        symptoms = models.SymptomName.objects.all()
        serializer = serializers.SymptomNameSerializer(symptoms, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request, year, month, day):
        symptom_ids = request.data.get('symptoms', [])
        symptom_date = date(year, month, day)
        created_symptoms = []

        for symptom_id in symptom_ids:
            symptom = get_object_or_404(models.SymptomName, id=symptom_id)
            user_symptom, created = models.UserSymptom.objects.get_or_create(
                symptom=symptom,
                user_id=request.user,
                date=symptom_date,
                defaults={'is_active': True}
            )
            if not created:
                user_symptom.is_active = True
                user_symptom.save()
            created_symptoms.append(user_symptom)

        serializer = serializers.SymptomResponseSerializer(created_symptoms, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
