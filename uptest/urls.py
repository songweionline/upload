from uptest.views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('b', UpTest, basename='lfte')


urlpatterns = ([
    path('a/', UpTest.as_view(), name='test'),
    path('up4/', ImageView.as_view(), name='up-list1'),
    path('ups4/<int:pk>/', ImageView.as_view(), name='up-detail1'),
])