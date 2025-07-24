from rest_framework import serializers
from .models import Task


class TaseSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'description', 'due_date', 'completed', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']
