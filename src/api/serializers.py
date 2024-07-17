from rest_framework import serializers

from visit_app.models import Store, Visit


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ["id", "name"]


class VisitRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ["store", "latitude", "longitude"]


class VisitResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ["id", "timestamp"]
