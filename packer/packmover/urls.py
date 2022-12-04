from django.urls import path
from packmover.views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('',view=Index,name='index'),
    path('login',view=Login,name='login'),
    path('addmin',view=Addmin,name='addmin'),
    path('logout',view=Logout,name='logout'),
    path('about',view=About,name='about'),
    path('contact',view=ContactP,name='contact'),
    path('add_service',view=Add_service,name='add_service'),
    path('service',view=Service,name='service'),
    path('new_booking',view=NewBook,name='new_booking'),
    path('view_bookingdetail/<int:id>',view=View_bdetail,name='view_bookingdetail'),
    path('old_booking',view=OldBook,name='old_booking'),
    path('user_request',view=UserR,name='user_request'),
    path('unread_quaries',view=UnreadQ,name='unread_quaries'),
    path('view_quaries.<int:id>',view=ViewQ,name='view_quaries'),
    path('search',view=Search,name='search'),
    path('bookbwdate',view=BookBwDate,name='bookbwdate'),
    path('quariesbwdate',view=QuariesBwDate,name='quariesbwdate'),
    path('changepassword',view=ChangePassword,name='changepassword'),
    
    path('read_quaries',view=ReadQ,name='read_quaries'),
    path('admin_base',view=Admin_base,name='admin_base'),
    path('manage_service',view=ManageS,name='manage_service'),
    path('edit_service/<int:id>',view=EditS,name='edit_service'),
    path('delete_service/<int:id>',view=DeleteS,name='delete_service'),
    path('deloldbooking/<int:id>',view=Deloldbooking,name='deloldbooking'),
    path('deletequaries/<int:id>',view=Deletequarie,name='deletequarie'),
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
