from rest_framework import serializers
from order.models import Shop, Menu, Order, Orderfood


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'shop_name', 'shop_address']
        
        
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'shop', 'food_name']