from django.shortcuts import render
from .models import Car
from .serializers import CarSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
# def car_details(request,pk):
#     res=Car.objects.get(id=pk)
#     serializer=CarSerializers(res)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

# def car_detailsall(request):
#     res=Car.objects.all()
#     serializer=CarSerializers(res,many=True)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

def postjsondata(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=CarSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data added ot created sucessfully'}
            json_data=JSONRenderer().render(res)
            print(json_data)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')