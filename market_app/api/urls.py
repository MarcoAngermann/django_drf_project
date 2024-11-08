from django.urls import path
from .views import markets_view, market_single_view, sellers_view

urlpatterns = [
    path('market/', markets_view),
    path('<int:pk>/', market_single_view),
    path('seller/', sellers_view)
]