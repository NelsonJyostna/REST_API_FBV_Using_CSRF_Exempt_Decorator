from rest_framework import serializers
from .models import Employee

class EmployeeSerialzier(serializers.Serializer):
    name=serializers.CharField(max_length=50)
    email=serializers.EmailField()
    password=serializers.CharField(max_length=50)
    phone=serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name= validated_data.get('name', instance.name)
        instance.email= validated_data.get('email', instance.email)
        instance.password=  validated_data.get('password', instance.password)
        instance.phone=  validated_data.get('phone', instance.phone)
        instance.save()
        return instance
