from .import views
from django.urls import path

urlpatterns = [
    
   path('',views.new),
   path('user.html',views.userDetails),
   path('types.html',views.typesbutton,name='types'),
   path('<str:t>',views.getDetails,name='detail')
    
]