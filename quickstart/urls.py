from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r'airplanes', views.AirplaneViewSet)

urlpatterns = router.urls