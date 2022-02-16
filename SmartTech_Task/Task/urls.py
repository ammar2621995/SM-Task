from django.urls import include , path
from .views import index,com_method,pro_method,doc_method,noti_method

urlpatterns = [
    path('',index, name = "ind"),
    path('Pro',pro_method, name = "Pro"),
    path('Doc',doc_method, name = "Doc"),
    path('Comment',com_method, name = "Com"),
    path('Notifi',noti_method, name = "Not"),
]
