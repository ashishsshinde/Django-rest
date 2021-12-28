from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import requests

# Create your views here.
def student_detail(request, pk):
    stu = Student.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many = True)
    # json_data = JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe = False)


def VisitData(request):
    URL = "http://127.0.0.1:8000/stuinfo"
    r = requests.get(url=URL)
    data = r.json()
    return render(request, 'index.html', {'response':data}) 