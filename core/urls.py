from django.contrib import admin
from django.urls import path, include
from delivery.views import OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order', OrderViewSet, basename='orders')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]