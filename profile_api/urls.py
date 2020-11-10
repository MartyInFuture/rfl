from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profile_api import views


# https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, 'hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]