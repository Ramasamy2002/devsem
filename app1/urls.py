from django.urls import path
from . import views
urlpatterns=[
    path('ex/',views.sample,name="sample"),
    path('es/',views.htmlren,name="htm"),
    path('data/',views.index,name="index"),
    path('data/add/',views.add,name="add"),
    path('data/add/addrecord',views.addrecord,name="addrecord"),
    path('data/delete/<int:id>',views.delete,name="delete"),
]
