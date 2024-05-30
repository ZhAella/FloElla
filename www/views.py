import datetime
from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from www.models import MenstrualDayStatus
from www.serializers import MenstrualDayStatusSerializer
from datetime import date, timedelta


class MenstrualDayStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        date_ = request.query_params.get("date")
        if date_ is None:
            date_ = datetime.date.today()
        user_id = request.user.id
        day_status = MenstrualDayStatus.objects.filter(date=date_, user_id=user_id).first()
        if day_status is not None:
            serializer = MenstrualDayStatusSerializer(day_status)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return JsonResponse('error: ', status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def put(request):
        date_ = request.query_params.get("date")
        if date_ is None:
            date_ = datetime.date.today()
        user_id = request.user.id
        status_ = request.data.get('status')
        user = request.user

        try:
            day_status = MenstrualDayStatus.objects.get(user_id=user_id, date=date_)
        except MenstrualDayStatus.DoesNotExist:
            return Response({"error": "No status found for today"}, status=status.HTTP_404_NOT_FOUND)

        before_date_ = date_ - timedelta(days=1)
        try:
            before_date_status = MenstrualDayStatus.objects.get(user_id=user_id, date=before_date_)
        except MenstrualDayStatus.DoesNotExist:
            before_date_status = None

        day_status.status = status_
        day_status.save()

        if status_ == 'periods':
            if before_date_status and before_date_status.status == 'periods':
                pass
            else:
                user.menstruation_start_date = date_
            user.menstruation_end_date = date_
        user.save()

        data = request.data
        serializer = MenstrualDayStatusSerializer(day_status, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSymptomAPIView(APIView):
    @staticmethod
    def put(request):
        date_ = request.query_params.get("date")
        if date_ is None:
            date_ = datetime.date.today()

        try:
            menstrual_day_status = MenstrualDayStatus.objects.get(date=date_)
        except MenstrualDayStatus.DoesNotExist:
            return Response({"error": "MenstrualDayStatus not found for the given date"},
                            status=status.HTTP_404_NOT_FOUND)

        symptoms_data = request.data.get('symptoms')
        serializer = MenstrualDayStatusSerializer(
            menstrual_day_status,
            data={"symptoms": symptoms_data}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserMenstrualDaysStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        queryset = MenstrualDayStatus.objects.filter(user_id=request.user.id)
        serializer = MenstrualDayStatusSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserMenstrualDaysWeekStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user_id = request.user.id
        today = date.today()
        week_ago = today - timedelta(days=7)
        queryset = MenstrualDayStatus.objects.filter(user_id=user_id, date__gte=week_ago, date__lte=today)
        serializer = MenstrualDayStatusSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserMenstrualDaysMonthStatusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user_id = request.user.id
        today = date.today()
        month_ago = today - timedelta(days=30)
        queryset = MenstrualDayStatus.objects.filter(user_id=user_id, date__gte=month_ago, date__lte=today)
        serializer = MenstrualDayStatusSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
