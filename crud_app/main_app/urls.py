from django.urls import path
from main_app import views

urlpatterns = [
  
    path('',views.index,name='index'),
    path('save_json',views.save_json,name='save_json'),
    path('update/<int:id>/', views.update_stock_data, name='update_stock_data'),
    path('Add_stock/',views.add_stock, name='Add_stock'),
    path('stock/delete/<int:id>/', views.delete, name='delete_stock'),
    path('stock/delete_stock_data/<int:id>/', views.delete_stock_data, name='delete_stock_data'),
]
