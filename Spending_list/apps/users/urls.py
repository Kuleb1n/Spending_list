from django.urls import path

from Spending_list.apps.users.views import LoginUserView, RegisterUserView, EmailConfirmationView

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('email-confirmation/<str:email>/<uuid:link>/', EmailConfirmationView.as_view(), name='email-confirmation'),
)
