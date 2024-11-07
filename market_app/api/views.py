from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import MarketSerializer
from market_app.models import Market

@api_view(['GET', 'POST'])
def markets_view(request):
    if request.method == 'GET':
        markets = Market.objects.all()
        serializer = MarketSerializer(markets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)