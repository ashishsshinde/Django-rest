from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .models import Agro
from .serializers import StudentSerializer
from .serializers import AgroSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import requests

# # Create your views here.
# def student_detail(request, pk):
#     stu = Student.objects.get(id = pk)
#     serializer = StudentSerializer(stu)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data)

# def student_list(request):
#     stu = Student.objects.all()
#     serializer = StudentSerializer(stu, many = True)
#     # json_data = JSONRenderer().render(serializer.data)
#     # return HttpResponse(json_data, content_type='application/json')
#     return JsonResponse(serializer.data, safe = False)

    # Create your views here.

# Create your views here.
def index(request):   
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        noofguest = request.POST.get('noofguest')
        typeofacc = request.POST.get('typeofacc')        
        Visit111 = Agro(fromdate=fromdate, todate=todate,
                         noofguest=noofguest, typeofacc=typeofacc)
        Visit111.save()


    data = {
        "title": "Home Page",
        "description": "BAAP AGRO!!!"
    }
    return render(request, 'index2.html', data)



def student_detail(request, pk):
    stu = Agro.objects.get(id = pk)
    serializer = AgroSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Agro.objects.all()
    serializer = AgroSerializer(stu, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe = False)



def VisitData(request):
    URL = "http://127.0.0.1:8000/stuinfo"
    r = requests.get(url=URL)
    data = r.json()
    return render(request, 'index.html', {'response':data}) 