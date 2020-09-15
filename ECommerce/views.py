from django.shortcuts import render
from .models import Machine,Pod
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from .serializer import  PodSerializer,MachineSerializer
from rest_framework.decorators import api_view
from django.http import HttpResponse

def fill_database(request):
    Pod.objects.all().delete()
    Machine.objects.all().delete()
    machine_list = [
    {'name': 'CM001','product_type': 'base model','water_line_compatible':False,'size':'small machine'},
    {'name': 'CM002','product_type':'premium model' ,'water_line_compatible':False,'size':'small machine'},
    {'name': 'CM003','product_type':'deluxe model' ,'water_line_compatible':True,'size':'small machine'},
    {'name': 'CM101','product_type':'base model' ,'water_line_compatible':False,'size':'large machine'},
    {'name': 'CM102','product_type':'premium model' ,'water_line_compatible':True,'size':'large machine'},
    {'name': 'CM103','product_type':'premium model' ,'water_line_compatible':True,'size':'large machine'},
    {'name': 'EM001','product_type':'base model' ,'water_line_compatible':False,'size':'espresso machine'},
    {'name': 'EM002','product_type':'premium model' ,'water_line_compatible':False,'size':'espresso machine'},
    {'name': 'EM003','product_type':'deluxe model' ,'water_line_compatible':True,'size':'espresso machine'}
    ]

    for m in machine_list:
        machine = Machine(name=m['name'],product_type=m['product_type'],water_line_compatible=m['water_line_compatible'],size=m['size'])
        machine.save()
    pod_list = [
        {'name':'CP001','product_type':'small','pack_size':1,'coffee_flavor':'vanilla'},
        {'name':'CP003','product_type':'small','pack_size':3,'coffee_flavor':'vanilla'},
        {'name':'CP011','product_type':'small','pack_size':1,'coffee_flavor':'caramel'},
        {'name':'CP013','product_type':'small','pack_size':3,'coffee_flavor':'caramel'},
        {'name':'CP021','product_type':'small','pack_size':1,'coffee_flavor':'psl'},
        {'name':'CP023','product_type':'small','pack_size':3,'coffee_flavor':'psl'},
        {'name':'CP031','product_type':'small','pack_size':1,'coffee_flavor':'mocha'},
        {'name':'CP033','product_type':'small','pack_size':3,'coffee_flavor':'mocha'},
        {'name':'CP041','product_type':'small','pack_size':1,'coffee_flavor':'hazelnut'},
        {'name':'CP043','product_type':'small','pack_size':3,'coffee_flavor':'hazelnut'},
        {'name':'CP101','product_type':'large','pack_size':1,'coffee_flavor':'vanilla'},
        {'name':'CP103','product_type':'large','pack_size':3,'coffee_flavor':'vanilla'},
        {'name':'CP111','product_type':'large','pack_size':1,'coffee_flavor':'caramel'},
        {'name':'CP113','product_type':'large','pack_size':3,'coffee_flavor':'caramel'},
        {'name':'CP121','product_type':'large','pack_size':1,'coffee_flavor':'psl'},
        {'name':'CP123','product_type':'large','pack_size':3,'coffee_flavor':'psl'},
        {'name':'CP131','product_type':'large','pack_size':1,'coffee_flavor':'mocha'},
        {'name':'CP133','product_type':'large','pack_size':3,'coffee_flavor':'mocha'},
        {'name':'CP141','product_type':'large','pack_size':1,'coffee_flavor':'hazelnut'},
        {'name':'CP143','product_type':'large','pack_size':3,'coffee_flavor':'hazelnut'},
        {'name':'EP003','product_type':'espresso','pack_size':3,'coffee_flavor':'vanilla'},
        {'name':'EP005','product_type':'espresso','pack_size':5,'coffee_flavor':'vanilla'},
        {'name':'EP007','product_type':'espresso','pack_size':7,'coffee_flavor':'vanilla'},
        {'name':'EP013','product_type':'espresso','pack_size':3,'coffee_flavor':'caramel'},
        {'name':'EP015','product_type':'espresso','pack_size':5,'coffee_flavor':'caramel'},
        {'name':'EP015','product_type':'espresso','pack_size':7,'coffee_flavor':'caramel'}
    ]

    for pod in pod_list:
        p = Pod(name = pod['name'],product_type=pod['product_type'],pack_size=pod['pack_size'],coffee_flavor=pod['coffee_flavor'])
        p.save()
    return HttpResponse("Database Filled")


@api_view(['GET'])
def get_machines(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        machines = Machine.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            machines = machines.filter(name__icontains=name)
        product_type = request.GET.get('product_type', None)
        if product_type is not None:
            machines = machines.filter(product_type__icontains=product_type)
        water_line_compatible = request.GET.get('water_line_compatible', None)
        if water_line_compatible is not None:
            machines = machines.filter(water_line_compatible=water_line_compatible)
        size = request.GET.get('size', None)
        if size is not None:
            machines = machines.filter(size__icontains=size)
        
        machines_serializer = MachineSerializer(machines, many=True)
        return JsonResponse(machines_serializer.data, safe=False)



@api_view(['GET'])
def get_pods(request):
    
    if request.method == 'GET':
        pods = Pod.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            pods = pods.filter(name__icontains=name)
        product_type = request.GET.get('product_type', None)
        if product_type is not None:
            pods = pods.filter(product_type__icontains=product_type)
        pack_size = request.GET.get('pack_size', None)
        if pack_size is not None:
            pods = pods.filter(pack_size=pack_size)
        coffee_flavor = request.GET.get('coffee_flavor', None)
        if coffee_flavor is not None:
            pods = pods.filter(coffee_flavor__icontains=coffee_flavor)
        
        pods_serializer = PodSerializer(pods, many=True)
        return JsonResponse(pods_serializer.data, safe=False)
        