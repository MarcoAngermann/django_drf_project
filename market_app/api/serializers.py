from rest_framework import serializers
from market_app.models import Market, Seller, Product

def validate_no_x(value):
        errors = []

        if 'X' in value:
            errors.append("no x in location")
        if 'Y' in value:
            errors.append("no y in location")
        
        if errors:
            raise serializers.ValidationError(errors)
        return value

class MarketSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    location = serializers.CharField(max_length=255, validators=[validate_no_x])
    description = serializers.CharField()
    net_worth = serializers.DecimalField(max_digits=100, decimal_places=2)

    def create(self, validated_data):
        return Market.objects.create(**validated_data)

    def update(self,instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.location = validated_data.get('location', instance.location)
        instance.description = validated_data.get('description', instance.description)
        instance.net_worth = validated_data.get('net_worth', instance.net_worth)
        instance.save()
        return instance
    
    # def validate_location(self, value):  Diese Funktion wird dafür genutzt um die Validierung der Location zu steuern
    #     if 'X' in value:
    #     raise serializers.ValidationError("no x in location")
    #     return value

class SellerDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    contact_info = serializers.CharField()
    markets = MarketSerializer(many=True, read_only=True)


class SellerCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    contact_info = serializers.CharField()
    markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    def validate_markets(self, value):
        markets = Market.objects.filter(id__in=value)
        if len(markets) != len(value):
            raise serializers.ValidationError("Invalid market ids")
        return value

    def create(self, validated_data):
        market_ids = validated_data.pop('markets')
        seller = Seller.objects.create(**validated_data)
        markets = Market.objects.filter(id__in=market_ids)
        seller.markets.set(markets)
        return seller
    

from rest_framework import serializers
from market_app.models import Market, Product

from rest_framework import serializers
from market_app.models import Market, Product, Seller

class ProductDetailSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    market = serializers.IntegerField(write_only=True)
    seller = serializers.IntegerField(write_only=True)  # Neues Feld für Seller ID
    price = serializers.DecimalField(max_digits=50, decimal_places=2)

    def validate_market(self, value):
        if not Market.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid market id")
        return value
    
    def validate_seller(self, value):
        if not Seller.objects.filter(id=value).exists():
            raise serializers.ValidationError("Invalid seller id")
        return value
    
    def create(self, validated_data):
        market_id = validated_data.pop('market')
        seller_id = validated_data.pop('seller')
        product = Product.objects.create(market_id=market_id, seller_id=seller_id, **validated_data)
        return product



{ 
    "name": "Produktname", 
    "description": "Produktbeschreibung", 
    "market": 2, 
    "seller": 1,
    "price": 9.99 
}