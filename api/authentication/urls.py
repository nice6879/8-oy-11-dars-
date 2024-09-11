from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
]


"""
access
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NzE0ODE4LCJpYXQiOjE3MjU3MTEyMTgsImp0aSI6IjNhZDZkMzEwODNmODQxM2I5ZmVkMzA2N2U4NGRhMDUyIiwidXNlcl9pZCI6MX0.SXOrETCDr8lJh6AjgYt7DbJ_leTpLAnXDg7aA6UNmSg

refresh
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTc5NzYxOCwiaWF0IjoxNzI1NzExMjE4LCJqdGkiOiI1ODY5ODk4YWE2NmI0ODc2YWIzNDkyNzMxNGI0YzY5ZCIsInVzZXJfaWQiOjF9.vlcztTPVs7YopWqIXgmVmbDo07iu2eKD8IziRhYMPtg
"""