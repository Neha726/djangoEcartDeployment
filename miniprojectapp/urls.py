from django.urls import path
from miniprojectapp import views
urlpatterns= [
      path('',views.home),
      path('register',views.register)
]