from django.urls import path
from .views import MarketsView, MarketDetails,SellerOfMarketList, sellers_view, products_view, product_single_view , sellers_single_view

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketDetails.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', sellers_view),
    path('product/', products_view),
    path('product/<int:pk>/', product_single_view),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single'),
]