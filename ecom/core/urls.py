from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, shop, signup, my_account, edit_my_account
from product.views import product


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/', my_account, name='myaccount'),
    path('myaccount/edit/', edit_my_account, name='edit_myaccount'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>/', product, name='product'),

]
