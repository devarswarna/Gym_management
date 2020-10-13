from django.contrib import admin
from django.urls import path
from gym.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name="home"),
    path('about',About,name="about"),
    path('contact',Contact,name="contact"),
    path('admin_login',Login,name="login"),
    path('logout',Logout_admin,name="logout"),

    path('add_enquiry',Add_enq,name="add_enquiry"),
    path('view_enquiry',View_enq,name="view_enquiry"),
    path('delete_enq(?P<int:pid>)',Delete_enq,name='delete_enq'),

    path('add_equipment',Add_Equipment,name="add_equipment"),
    path('view_equipment',View_Equipment,name="view_equipment"),
    path('delete_equipment(?P<int:pid>)',Delete_Equipment,name='delete_equipment'),

    path('add_plan',Add_Plan,name="add_plan"),
    path('view_plan',View_Plan,name="view_plan"),
    path('delete_plan(?P<int:pid>)',Delete_Plan,name='delete_plan'),

    path('add_member',Add_Member,name='add_member'),
    path('view_member',View_Member,name="view_member"),
    path('delete_memmber(?P<int:pid>)',Delete_Memeber,name='delete_memmber'),



]
