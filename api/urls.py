from django.urls import path, include
from . import views
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('quiz/detail/<int:id>/', views.quizDetailView),
    path('answer/create/<int:id>/', views.createQuizAnswer),
    path('authentication/', include('api.authentication.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# ACCESS -> Ishlash uchun
# REFRESH -> Access token olish uchun 

"""
access
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1NzE0ODE4LCJpYXQiOjE3MjU3MTEyMTgsImp0aSI6IjNhZDZkMzEwODNmODQxM2I5ZmVkMzA2N2U4NGRhMDUyIiwidXNlcl9pZCI6MX0.SXOrETCDr8lJh6AjgYt7DbJ_leTpLAnXDg7aA6UNmSg

refresh
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyNTc5NzYxOCwiaWF0IjoxNzI1NzExMjE4LCJqdGkiOiI1ODY5ODk4YWE2NmI0ODc2YWIzNDkyNzMxNGI0YzY5ZCIsInVzZXJfaWQiOjF9.vlcztTPVs7YopWqIXgmVmbDo07iu2eKD8IziRhYMPtg
"""