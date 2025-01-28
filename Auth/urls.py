from django.urls import path,include
from rest_framework import routers
from .ViewsetLogin import signup_view, login_view
router = routers.SimpleRouter()

urlpatterns = [
    path('', include(router.urls)), 
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]