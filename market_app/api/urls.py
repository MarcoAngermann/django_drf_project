from django.urls import path, include
from .views import ProductsViewSet,MarketsView, MarketDetails,SellerOfMarketList, sellers_view, products_view, product_single_view , sellers_single_view
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'products', ProductsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetails.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', sellers_view),
    path('product/', products_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller-detail'),
]