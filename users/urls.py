from django.urls import path
# from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .views import CustomObtainJSONWebToken

app_name = 'users'
urlpatterns = [
    path('api-token-auth/', CustomObtainJSONWebToken.as_view()),
    path('api-token-refresh/', RefreshJSONWebToken.as_view()),
    path('api-token-verify/', VerifyJSONWebToken.as_view())
]
