from . import views
from django.urls import path,include

from auction_project import settings


urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register, name='register'),
    path('login/',views.login, name='login'),
    path('logout/', views.my_logout_view, name='logout'),
    path('products',views.products,name='products'),
    path('productdetail/<int:product_id>/',views.productdetail,name='productdetail'),
    path('save_bid/',views.save_bid,name='save_bid'),
    path('success',views.success,name='success')
]