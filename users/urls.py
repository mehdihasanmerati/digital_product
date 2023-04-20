from django.urls import path
from .views import RegisterView, GetTokenView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('register/', RegisterView.as_view()),
   # path('get-token/', GetTokenView.as_view()), # چون از یوزرزتوکن، جی دبیلیو تی، استفاده می کنبم دیگر به گت توکن نیاز نداریم

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]