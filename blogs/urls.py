from django.urls import path
# from rest_framework import routers
from .views import BlogListView

app_name = 'blogs'
#
# router = routers.DefaultRouter()
# router.register('blogs', BlogView)

urlpatterns = [
    path('', BlogListView.as_view())
    # path('', include(router.urls))
]
