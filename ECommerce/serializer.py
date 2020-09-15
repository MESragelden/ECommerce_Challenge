from rest_framework import serializers 
from .models import Machine,Pod
 
 
class MachineSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Machine
        fields = ('name',
                  'product_type',
                  'water_line_compatible',
                  'size')

class PodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pod
        fields = ('name',
                  'product_type',
                  'pack_size',
                  'coffee_flavor')