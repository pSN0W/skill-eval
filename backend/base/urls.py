from django.urls import path

from . import views

urlpatterns = [
    path('',views.get_routes,name="routes"),
    path('login/', views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('users/create',views.create_user,name="users-create"),
]