from django.urls import path
from . import views 


urlpatterns = [
    
    path('',views.dashboard,name='dashboard'),
    path('/add/',views.add,name='add'),
    path('/transactionlist/',views.transaction_list,name='transactionlist'),
    path('/edit/<int:pk>',views.update,name='edit'),
    path('/delete/<int:pk>',views.delete,name='delete'),
]