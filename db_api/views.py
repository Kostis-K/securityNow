from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
import json
#import

geia_sas_message = "GEIA SAS"
# Create your views here.
class StartView(APIView): #securityNow/hello
    def get(self, request, *args, **kwargs):
        print(geia_sas_message)
        return Response(geia_sas_message, status=status.HTTP_200_OK)
class EmployeeApiView(APIView): #securityNow/employee
    def post(self, request, *args, **kwargs):
        print("Post request called....!!!!! Up in here...!!")
        serializer = EmployeeSerializer(data=request.data)
        print("**** request dataaa ****")
        print(request.data)
        print("**** **** **** **** ****")
        try:
            if serializer.is_valid():
                data = self.createEmployeeObj(request)
                Employee(data=data).update()
                #Employee.objects(data=data).save()
                return Response(data, status=status.HTTP_201_CREATED)
        except Exception as exxx:
            return Response(str(exxx), status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                #serializer.save() #gia kapoio logo den katafera na swsw sth vash katey8eian to diserialized object...
                # print("***** serializer data ****") #Gia kapoio logo o serializer ta kanei mantAra... Den katafera na ton ftia3w na pai3ei swsta kai ayto me tsantizei...
                # print(serializer.data)
                # print("**** **** **** **** ****")
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except Exception as exxx:
        #     return Response(str(exxx), status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def createEmployeeObj(self, request): #helper function since I didn't manage to serialize properly the Employee in request...
        data = {
            'username' : request.data.get('username'),
            'first_name' : request.data.get('firstname'),
            'last_name' : request.data.get('lastname'),
            'gender' : request.data.get('gender'),
            'cs_user_status' : request.data.get('cs_user_status'),  # Auto einai h Trexousa Katastash 1A
            'job_position' : request.data.get('job_position'),  # 1B
            'desirable_sector' : request.data.get('desirable_sector'),  # 2
            'cs_specialisms' : request.data.get('cs_specialisms'),  # 2A & 2B
            'desirable_country' : request.data.get('desirable_country'),  # 3
            'desirable_area_perifereia' : request.data.get('desirable_area_perifereia'),  # values from lat_long Collection (Perifereia_gr) #4
            'desirable_area_dhmos' : request.data.get('desirable_area_dhmos'),  # values from lat_long Collection (Dhmos_gr) #5
            'desirable_work_type' : request.data.get('desirable_work_type'),  # 6
            'desirable_schedule' : request.data.get('desirable_schedule'),  # 7
            'min_wromis8io' : request.data.get('min_wromis8io'),  # 8
            'min_mis8os' : request.data.get('min_mis8os'),  # 9
            'karta_anergias' : request.data.get('karta_anergias'),  # 10
            'adeia_asfaleias' : request.data.get('adeia_asfaleias'),  # 11
            'adeiaIX' : request.data.get('adeiaIX'),  # 12
            'adeiaDikyklo' : request.data.get('adeiaDikyklo'),  # 13
            'education_level' : request.data.get('education_level'),  # 14
            'agglika' : request.data.get('agglika'),  # 15
            'allh_glwssa' : request.data.get('allh_glwssa'),  # Kamia, mia h kai parapanw alles glwsses #15A
            'cctv' : request.data.get('cctv'),  # 16
            'pc' : request.data.get('pc'),  # 17
            'mouseia' : request.data.get('mouseia'),  # 18
            'x_ray_screener' : request.data.get('x_ray_screener'),  # 19
            'first_aid' : request.data.get('first_aid'),  # 20
            'lifeguard' : request.data.get('lifeguard'),  # 21
            'limenikes_egk' : request.data.get('limenikes_egk'),  # 22
            'epoptes_arxi' : request.data.get('epoptes_arxi'),  # 23
            'vip' : request.data.get('vip'),  # 24
            'oplokatoxh' : request.data.get('oplokatoxh'),  # 25
            'polemikes_texnes' : request.data.get('polemikes_texnes'),  # 26
            'drone' : request.data.get('drone'),  # 27
            'military_obligations' : request.data.get('military_obligations'),  # 28
            'physic_and_endurance' : request.data.get('physic_and_endurance'),  # 29
            'appearance' : request.data.get('appearance'),  # 30
            'supervision_inspection' : request.data.get('supervision_inspection'),  # 31
            'communications_skills' : request.data.get('communications_skills'),  # 32
            'reflexes_on_danger' : request.data.get('reflexes_on_danger'),  # 33
            'professionalism' : request.data.get('professionalism'),  # 34
            'confidentiality' : request.data.get('confidentiality'),  # 35
        }