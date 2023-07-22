from django.urls import path

from apps.users.views import LoginUserView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
)
