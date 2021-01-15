from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from passlib.hash import django_pbkdf2_sha256 as handler
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from .models import Signup,SerSignup
from fcm_django.models import FCMDevice

class User_Signup(APIView):

    def get(self,request):

        
        try:

            data = Signup.objects.all()
            serializer = SerSignup(data,many=True)
            message={

                'status' : True,
                'data':serializer.data

            }
            
             


            return Response(message)
        except:
            message={
                'status' : False,

            }
            return Response(message)




    def post(self , request):
        try:

       

            Full_Name=request.data.get('Full_Name')
            Email=request.data.get('Email')
            Username=request.data.get('Username')
            Password=request.data.get('Password')
            Password=handler.hash(Password)
            Image=request.FILES.get('Image')
            Sender_ID=request.data.get('Sender_ID')
            Device_type=request.data.get('Device_type')
            latitude=request.data.get('latitude')
            longitude=request.data.get('longitude')

            

            checkEmailExist = Signup.objects.filter(Email = Email)
            if checkEmailExist:
                message = {
                "status" : False,
                'message' : "Email Already Exist",

                }
                return Response(message)

            checkUserName = Signup.objects.filter(Username = Username)
            if checkUserName:
                message = {
                'status' : False,
                'message' : "UserName Already Exist",

                }
                return Response(message)


            data = Signup(Full_Name = Full_Name , Username = Username,Email = Email,Password = Password,Sender_ID = Sender_ID,Device_type= Device_type,Image  = Image,latitude = latitude,longitude = longitude)
            data.save()

            userid = data.id

            try:

                fcm = FCMDevice(registration_id = Sender_ID,name = userid,type = Device_type)
                fcm.save()

            except:
                None

            fetch_userobeject = Signup.objects.get(Username = Username)
            serdata = SerSignup(fetch_userobeject)

            message = {

                "status" : True,
                "message" : "Account Created Successfully",
                "data" : serdata.data


            }

            return Response(message)


        except Exception as e:

            data={
                    'status' : False,
                    'message': str(e)
                }
            return Response(data)



###patient login

class Login(APIView):
    def post(self,request):
        try:

            Username=request.data.get('Username')
            Password=request.data.get('Password')
            Sender_ID = request.data.get('Sender_ID')
            Device_type = request.data.get('Device_type')
            latitude=request.data.get('latitude')
            longitude=request.data.get('longitude')

            authenticate = Signup.objects.filter(Username=Username)



            

            if authenticate:
                authenticate = authenticate[0]



                


                if handler.verify(Password,authenticate.Password):


                    authenticate.Sender_ID=Sender_ID
                    authenticate.Device_type=Device_type
                    authenticate.save()


                    id = authenticate.id


                    fcm = FCMDevice.objects.filter(name = id)
                    if fcm:
                        fcm = fcm[0]

                        

                    
                        fcm.registration_id = Sender_ID
                        fcm.type = Device_type
                        fcm.save()


                        userdata = SerSignup(authenticate)
                        message={
                        'status' : True,
                        'message':'Successfully Login',
                        'data' : userdata.data,


                        }

                        return Response(message)


                        
                    else:
                        pass

                else:
                    message={
                    'message':'Username or Password Does Not Match'
                }

                    return Response(message)

                

            else:

                message={
                        'message':'Username or Password Does Not Match'
                    }

                return Response(message)


        except Exception as e:
            message={
                    'status' : False,
                    'message': str(e)
                }
            return Response(message)