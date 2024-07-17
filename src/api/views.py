from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import (
    StoreSerializer,
    VisitRequestSerializer,
    VisitResponseSerializer,
)
from visit_app.authentication import PhoneAuthentication
from visit_app.models import Store


class StoreListView(APIView):
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        employee = request.user
        stores = Store.objects.filter(employee=employee)
        if not stores.exists():
            return Response({"error": "No stores found for this employee."}, status=status.HTTP_404_NOT_FOUND)
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)


class VisitCreateView(APIView):
    authentication_classes = [PhoneAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        employee = request.user
        serializer = VisitRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        store = serializer.validated_data.get("store")
        if not Store.objects.filter(id=store.id, employee=employee).exists():
            return Response({"error": "The employee is not tied to the store"}, status=status.HTTP_400_BAD_REQUEST)
        serializer.validated_data.update({"employee": employee})
        visit = serializer.save()
        serializer = VisitResponseSerializer(visit)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
