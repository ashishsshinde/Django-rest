from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)




class AgroSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    fromdate = serializers.CharField(max_length=100)   
    todate = serializers.CharField(max_length=100)
    noofguest = serializers.CharField(max_length=100)
    typeofacc = serializers.CharField(max_length=100)