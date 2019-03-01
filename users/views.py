from django.shortcuts import render

from rest_framework_jwt.views import ObtainJSONWebToken, RefreshJSONWebToken, VerifyJSONWebToken
from .serializers import CustomJWTSerializer


class CustomObtainJSONWebToken(ObtainJSONWebToken):
    serializer_class = CustomJWTSerializer


# class CustomRefreshWebToken(RefreshJSONWebToken):
#     serializer_class = CustomJWTSerializer
#
#
# class CustomVerifyWebToken(VerifyJSONWebToken):
#     serializer_class = CustomJWTSerializer
