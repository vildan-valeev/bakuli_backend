from django.urls import path

from users.views import ProfileDetail, ProfileCreate, ProfileUpdate, ProfileDetailMe

urlpatterns = [
    path('create/', ProfileCreate.as_view()),
    path('detail/<int:pk>/', ProfileDetail.as_view()),
    path('detail/me/', ProfileDetailMe.as_view()),
    path('update/<int:pk>/', ProfileUpdate.as_view()),

]
