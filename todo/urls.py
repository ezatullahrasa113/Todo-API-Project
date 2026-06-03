from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import TodoViewSet,RegisterView,LogoutView

router = DefaultRouter()
router.register('todo', TodoViewSet,basename='todo')


urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('logout/',LogoutView.as_view()),

]


urlpatterns += router.urls