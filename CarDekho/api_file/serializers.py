from rest_framework import serializers
from ..models import Carlist, Showroomlist

# Validators
def alphanumeric(value):
    if not str(value).isalnum():
        raise serializers.ValidationError("Only alphanumeric characters are allowed")
    
# class CarSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField(read_only = True)
#     chassisnumber = serializers.CharField(validators = [alphanumeric])
#     price = serializers.DecimalField(max_digits=10, decimal_places=2)
    
#     def create(self, validated_data):
#         return Carlist.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.chassisnumber = validated_data.get('chassisnumber',instance.chassisnumber)
#         instance.price = validated_data.get('price',instance.price)
#         instance.save()
#         return instance

# SERIALIZER CLASS FOR SHOWROOMLIST
class ShowroomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Showroomlist
        fields = "__all__"


#SERIALIZER CALSS FOR CARLIST
class CarSerializer(serializers.ModelSerializer):
    discount_price = serializers.SerializerMethodField()
    class Meta:
        model = Carlist
        # if we want to all fiels of the model
        fields = "__all__" 
        # another way is to list all fields
        # fields = ['name','id','description']
        
        # if we have alot of feilds and want ro exclude some of them
        # exclude = ['name']
    
    # LEARNING VALIDATIONS 
    
    # FIELD LEVEL VALIDATIONS
    
    def get_discount_price(self,object):
        dicountPrice = object.price - 5000
        return dicountPrice
    
    def validate_price(self, value):
        if value is not None:
            if value <= 20000.00 :
                raise serializers.ValidationError("Price must be greater than 20000")
            return value
        else:
            raise serializers.ValidationError("Enter a non null value ")
    
    
    # Object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description can not be same ")
        return data
    
    # Validators
    