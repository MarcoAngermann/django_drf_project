from rest_framework import serializers
from market_app.models import Market, Seller, Product

# def validate_no_x(value): #Dient als Beispiel
#         errors = []

#         if 'X' in value:
#             errors.append("no x in location")
#         if 'Y' in value:
#             errors.append("no y in location")
        
#         if errors:
#             raise serializers.ValidationError(errors)
#         return value

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'

    def validate_name(self, value):
        errors = []

        if 'X' in value:
            errors.append("no x in location")
        if 'Y' in value:
            errors.append("no y in location")
        
        if errors:
            raise serializers.ValidationError(errors)
        return value
    
class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets')
        
    class Meta:
        model = Seller
        exclude = []

class SellerDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Seller
            fields = '__all__'

# class SellerDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     contact_info = serializers.CharField()
#     markets = MarketSerializer(many=True, read_only=True)


# class SellerCreateSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     contact_info = serializers.CharField()
#     markets = serializers.ListField(child=serializers.IntegerField(), write_only=True)

#     def validate_markets(self, value):
#         markets = Market.objects.filter(id__in=value)
#         if len(markets) != len(value):
#             raise serializers.ValidationError("Invalid market ids")
#         return value

#     def create(self, validated_data):
#         market_ids = validated_data.pop('markets')
#         seller = Seller.objects.create(**validated_data)
#         markets = Market.objects.filter(id__in=market_ids)
#         seller.markets.set(markets)
#         return seller


class ProductDetailSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(max_length=255)
    # description = serializers.CharField()
    # market = serializers.IntegerField(write_only=True)
    # seller = serializers.IntegerField(write_only=True)  # Neues Feld für Seller ID
    # price = serializers.DecimalField(max_digits=50, decimal_places=2)

    # def validate_market(self, value):
    #     if not Market.objects.filter(id=value).exists():
    #         raise serializers.ValidationError("Invalid market id")
    #     return value
    
    # def validate_seller(self, value):
    #     if not Seller.objects.filter(id=value).exists():
    #         raise serializers.ValidationError("Invalid seller id")
    #     return value
    
    # def create(self, validated_data):
    #     market_id = validated_data.pop('market')
    #     seller_id = validated_data.pop('seller')
    #     product = Product.objects.create(market_id=market_id, seller_id=seller_id, **validated_data)
    #     return product
    
    # def update(self,instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.description = validated_data.get('description', instance.description)
    #     instance.price = validated_data.get('price', instance.price)
    #     instance.market = validated_data.get('market', instance.market)
    #     instance.seller = validated_data.get('seller', instance.seller)
    #     instance.save()
    #     return instance

    class Meta: # Das ersetzt den ganzen Code oben drüber !!!
        model = Product
        fields = '__all__'

 
# { 
#     "name": "Produktname", 
#     "description": "Produktbeschreibung", 
#     "market": 2, 
#     "seller": 1,
#     "price": 9.99 
# }