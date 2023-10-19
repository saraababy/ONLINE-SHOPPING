from django.urls import path
from Frondend import views

urlpatterns = [path('Home_admin/', views.Home_admin, name='Home_admin'),
               path('shop_now/', views.shop_now, name='shop_now'),
               path('login_Reg/', views.login_Reg, name='login_Reg'),
               path('signup/', views.signup, name='signup'),
               path('user_login/', views.user_login, name='user_login'),
               path('user_logout/', views.user_logout, name='user_logout'),
               path('about_us/', views.about_us, name='about_us'),
               path('contact_us/', views.contact_us, name='contact_us'),
               path('send_msg/', views.send_msg, name='send_msg'),
                path('pro_details/<int:dataid>/', views.pro_details, name='pro_details'),
                path('submitCart/', views.submitCart, name="submitCart"),
                path('DisplayCart/', views.DisplayCart, name="DisplayCart"),
                path('DeleteItem/<int:dataid>/', views.DeleteItem, name="DeleteItem"),
path('checkout/', views.checkout, name="checkout"),
path('orders/', views.orders, name="orders"),
path('profile/', views.profile, name="profile"),
path('update_profile/<int:dataid>', views.update_profile, name="update_profile"),
path('update_profileimage/<int:dataid>', views.update_profileimage, name="update_profileimage"),

               ]