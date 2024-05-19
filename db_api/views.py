from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Employee#, SpecialismType
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
        #serializer = EmployeeSerializer(data=request.data)
        print("**** request data ****")
        print(request.data)
        serializer = EmployeeSerializer(data=self.getData(request))
        print("**** serializer dataaa ****")
        #print(request.data)
        #print("**** **** **** **** ****")
        try:
            if serializer.is_valid():
                #data = self.createEmployeeObj(request)
                #Employee(data=data).update()
                print(serializer.validated_data)
                print('Step 1')
                employee_inst = serializer.save()
                #emplObj = self.createEmployeeObj2(request)
                print('Step 2')
                #Employee.objects.insert(emplObj)
                #emplObj.save()
                print('Step 333')
                #emplObj2 = self.createEmployeeObj3(request)
                #Employee.objects.insert(emplObj2)
                #print('Step 4')
                #Employee.objects(data=data).save()
                return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        except Exception as exxx:
            print('%%% Catch HERE BAD REQUESTTT.... %%%')
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

    def getData(self, request): #helper function since I didn't manage to serialize properly the Employee in request...
        data = {
            'username' : request.data.get('username'),
            'first_name' : request.data.get('first_name'),
            'last_name' : request.data.get('last_name'),
            'gender' : request.data.get('gender'),
            'cs_user_status' : request.data.get('cs_user_status'),  # Auto einai h Trexousa Katastash 1A
            'job_position' : request.data.get('job_position'),  # 1B
            'desirable_sector' : request.data.get('desirable_sector'),  # 2
            #'desirable_sector' : [SpecialismType(value) for value in request.data.get('desirable_sector', [])],
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
        return data

    # def createEmployeeObj2(self, request): #helper function since I didn't manage to serialize properly the Employee in request...
    #     emplObj = Employee()
    #     emplObj.username=request.data.get('username')
    #     print(f'--Username:{emplObj.username}-->')
    #     emplObj.first_name=request.data.get('firstname')
    #     emplObj.last_name=request.data.get('lastname')
    #     emplObj.gender=request.data.get('gender')
    #     emplObj.cs_user_status=request.data.get('cs_user_status')  # Auto einai h Trexousa Katastash 1A
    #     emplObj.job_position=request.data.get('job_position')  # 1B
    #     emplObj.desirable_sector=request.data.get('desirable_sector')  # 2
    #     emplObj.cs_specialisms=request.data.get('cs_specialisms'),  # 2A & 2B
    #     emplObj.desirable_country=request.data.get('desirable_country')  # 3
    #     emplObj.desirable_area_perifereia=request.data.get('desirable_area_perifereia')  # values from lat_long Collection (Perifereia_gr) #4
    #     emplObj.desirable_area_dhmos=request.data.get('desirable_area_dhmos')  # values from lat_long Collection (Dhmos_gr) #5
    #     emplObj.desirable_work_type=request.data.get('desirable_work_type')  # 6
    #     emplObj.desirable_schedule=request.data.get('desirable_schedule')  # 7
    #     emplObj.min_wromis8io=request.data.get('min_wromis8io')  # 8
    #     emplObj.min_mis8os=request.data.get('min_mis8os')  # 9
    #     emplObj.karta_anergias=request.data.get('karta_anergias')  # 10
    #     emplObj.adeia_asfaleias=request.data.get('adeia_asfaleias')  # 11
    #     emplObj.adeiaIX=request.data.get('adeiaIX') # 12
    #     emplObj.adeiaDikyklo=request.data.get('adeiaDikyklo')  # 13
    #     emplObj.education_level=request.data.get('education_level')  # 14
    #     emplObj.agglika=request.data.get('agglika') # 15
    #     emplObj.allh_glwssa=request.data.get('allh_glwssa')  # Kamia, mia h kai parapanw alles glwsses #15A
    #     emplObj.cctv=request.data.get('cctv')  # 16
    #     emplObj.pc=request.data.get('pc')  # 17
    #     emplObj.mouseia=request.data.get('mouseia')  # 18
    #     emplObj.x_ray_screener=request.data.get('x_ray_screener')  # 19
    #     emplObj.first_aid=request.data.get('first_aid')  # 20
    #     emplObj.lifeguard=request.data.get('lifeguard')  # 21
    #     emplObj.limenikes_egk=request.data.get('limenikes_egk')  # 22
    #     emplObj.epoptes_arxi=request.data.get('epoptes_arxi')  # 23
    #     emplObj.vip=request.data.get('vip') # 24
    #     emplObj.oplokatoxh=request.data.get('oplokatoxh')  # 25
    #     emplObj.polemikes_texnes=request.data.get('polemikes_texnes')  # 26
    #     emplObj.drone=request.data.get('drone')  # 27
    #     emplObj.military_obligations=request.data.get('military_obligations')  # 28
    #     emplObj.physic_and_endurance=request.data.get('physic_and_endurance')  # 29
    #     emplObj.appearance=request.data.get('appearance')  # 30
    #     emplObj.supervision_inspection=request.data.get('supervision_inspection')  # 31
    #     emplObj.communications_skills=request.data.get('communications_skills')  # 32
    #     emplObj.reflexes_on_danger=request.data.get('reflexes_on_danger')  # 33
    #     emplObj.professionalism=request.data.get('professionalism') # 34
    #     emplObj.confidentiality=request.data.get('confidentiality') # 35
    #     print('$$$$$$ START EMPLOYEE $$$$$$')
    #     print(emplObj)
    #     print('$$$$$$ END EMPLOYEE $$$$$$')
    #     return emplObj
    #
    # def createEmployeeObj3(self, request):  # helper function since I didn't manage to serialize properly the Employee in request...
    #     emplObj = Employee()
    #     emplObj.username = request.data.get('username')
    #     print(f'--Username.3:{emplObj.username}-->')
    #     emplObj.first_name = request.data.get('firstname')
    #     emplObj.last_name = request.data.get('lastname')
    #     emplObj.gender = request.data.get('gender')
    #     return emplObj