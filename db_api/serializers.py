import mongoengine
from rest_framework_mongoengine import serializers
from .models import Employee, Specialism
from mongoengine import fields
import enum

class SpecialismSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Specialism
        fields = ('specialism', 'specialism_time_from', 'specialism_time_to')

class EmployeeSerializer(serializers.EmbeddedDocumentSerializer):
    cs_specialisms = SpecialismSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('username',
                  'first_name',
                  'last_name',
                  'gender',
                  'cs_user_status',
                  'job_position',
                  'desirable_sector',
                  'cs_specialisms',
                  'desirable_country',
                  'desirable_area_perifereia',
                  'desirable_area_dhmos',
                  'desirable_work_type',
                  'desirable_schedule',
                  'min_wromis8io',
                  'min_mis8os',
                  'karta_anergias',
                  'adeia_asfaleias',
                  'adeiaIX',
                  'adeiaDikyklo',
                  'education_level',
                  'agglika',
                  'allh_glwssa',
                  'cctv',
                  'pc',
                  'mouseia',
                  'x_ray_screener',
                  'first_aid',
                  'lifeguard',
                  'limenikes_egk',
                  'epoptes_arxi',
                  'vip',
                  'oplokatoxh',
                  'polemikes_texnes',
                  'drone',
                  'military_obligations',
                  'physic_and_endurance',
                  'appearance',
                  'supervision_inspection',
                  'communications_skills',
                  'reflexes_on_danger',
                  'professionalism',
                  'confidentiality')

    # def to_representation(self, instance):
    #     json_inst = instance.to_json()
    #     print(f'******{json_inst}******')
    #     return json_inst

    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        #employee = Employee(**validated_data)  # <--
        #employee.save()  # <--
        return employee
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     for field_name, field in representation.items():
    #         #print(f'{field_name}-{field[0]} --')
    #         #if isinstance(field[0], fields.StringField):
    #         #    print(f'{field_name} is StringField..!!')
    #             #representation[field] = str(value)#because StringField is not serializable to kerato mou
    #         if isinstance(field[0], fields.StringField):
    #             value = str(field[0])
    #         elif isinstance(field[0], fields.EnumField):
    #             value = str(field[0].to_python(field[0]))
    #         if value is not None:
    #             representation[field_name] = value
    #     return representation
'''
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        for field_name, field in instance.items():
            # if field_name == 'cs_specialisms':
            #     serialized_specialisms = []
            #     for specialism in field:
            #         serialized_specialisms.append({
            #             'specialism': str(specialism['specialism']),
            #             'specialism_time_from': str(specialism['specialism_time_from']),
            #             'specialism_time_to': str(specialism['specialism_time_to'])
            #         })
            #     representation[field_name] = serialized_specialisms
            print(f'**field_name={field_name}, field={field}**')
            if isinstance(field, list):
                # Serialize list fields if needed
                representation[field_name] = [str(item) for item in field]
            elif isinstance(field, tuple):
                # Convert Enum fields to string
                print(f'Is the tuple a String?? {field_name} is {type(field)}??: tuple:#{field}#')
                representation[field_name] = str(field[0])
            elif isinstance(field, dict):
                representation[field_name] = {key: str(value) for key, value in field.items()}
            # elif isinstance(field, mongoengine.base.datastructures.BaseList):
            #     representation[field_name] = [str(item) for item in field]
            # elif isinstance(field, mongoengine.base.datastructures.BaseDict):
            #     # Convert mongoengine DictField to string values
            #     representation[field_name] = {key: str(value) for key, value in field.items()}
            elif hasattr(instance, field_name):
                value = getattr(instance, field_name)
                print(f'IS THIS A STRING?? {field_name} -- {representation[field_name]} <--')
                if hasattr(value, 'to_mongo'):
                    representation[field_name] = str(value.to_mongo())
                #print(f'StringField: {representation[field_name]} <--')
                else:
                    representation[field_name] = value
                    #print(f'Different type of field!!!: {type(field[0])}')
        return representation '''

