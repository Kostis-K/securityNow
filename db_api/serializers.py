from rest_framework_mongoengine import serializers
from .models import Employee, Specialism


class SpecialismSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Specialism
        fields = '__all__'

class EmployeeSerializer(serializers.EmbeddedDocumentSerializer):
    #cs_specialisms = SpecialismSerializer()
    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee