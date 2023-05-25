from . import views
from django.urls import path

urlpatterns =[
    path("",views.index,name="index"),
    path("brian",views.brian,name="brian"),
    path("sonu",views.sonu,name="sonu"),
    path("<str:name>",views.greet,name="greet")
]