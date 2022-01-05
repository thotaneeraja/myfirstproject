from.views import func
from django.urls import path,include
from.views import create,edit,update,delete,home,cre,index
urlpatterns=[
          path('neeru/',func),
          path('teja/',cre),
          path('index/',index),
          path('kesavulu/',create),
          path("edit/<str:name>/",edit),
          path('update/<str:name>/',update),
          path('delete/<str:name>/',delete),
          path('',home),

]