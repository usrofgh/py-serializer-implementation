from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(required=True)
    model = serializers.CharField(required=True)
    horse_powers = serializers.IntegerField(required=True)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(required=False)

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get("manufacturer", instance.manufacturer)
        instance.model = validated_data.get("model", instance.model)

        instance.horse_power = validated_data.get(
            "horse_power", instance.horse_power
        )

        instance.is_broken = validated_data.get(
            "is_broken", instance.is_broken
        )

        instance.problem_description = validated_data.get(
            "problem",
            instance.problem_description
        )
        instance.save()
        return instance
