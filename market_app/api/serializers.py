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

    sellers = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='seller_single') 

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
    
class MarketHyperlinkedSerializer(MarketSerializer,serializers.HyperlinkedModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    sellers = None
    class Meta:
        model = Market
        fields = ['id', 'url', 'name', 'location', 'description', 'net_worth']
    
class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(),
        many=True,
        write_only=True,
        source='markets')
    market_count = serializers.SerializerMethodField()
    class Meta:
        model = Seller
        fields = ['id', 'name', 'market_count', 'contact_info', 'markets', 'market_ids']
    
    def get_market_count(self, obj):
        return obj.markets.count()
    
class SellerListSerializer(SellerSerializer, serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seller
        fields = ['url', 'name', 'market_ids', 'market_count', 'contact_info']

# class SellerDetailSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Seller
#             fields = '__all__'

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


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

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