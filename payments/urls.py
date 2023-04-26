from django.urls import path
from .views import GatewayView, PaymentView

urlpatterns = [
    path('gatways/', GatewayView.as_view()),
    path('payments/', PaymentView.as_view())
]