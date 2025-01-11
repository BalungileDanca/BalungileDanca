from rest_framework import serializers
from datetime import date
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < date.today():
            raise serializers.ValidationError("The due date must be in the future.")
        return value

    def validate_priority_level(self, value):
        allowed_levels = ['Low', 'Medium', 'High']
        if value not in allowed_levels:
            raise serializers.ValidationError(f"Priority level must be one of {', '.join(allowed_levels)}.")
        return value

    def validate_status(self, value):
        allowed_statuses = ['Pending', 'Complete']
        if value not in allowed_statuses:
            raise serializers.ValidationError(f"Status must be one of {', '.join(allowed_statuses)}.")
        return value