from django.conf.urls.static import static
from django.urls import path

from onlinefoodmarket import settings
from yash import views

urlpatterns = [
    path('',views.showIndex,name="yash_admin"),
    path('login_check',views.login_check,name="login_check"),
    path('welcome',views.welcome,name="welcome"),



                      #state
    path('openstate',views.openstate,name="openstate"),
    path('opencity', views.opencity, name="opencity"),
    path('savestate',views.addingstate,name="savestate"),
    path('updatestate/', views.updatestate, name='updatestate'),
    path('updatestateid/', views.updatestateid, name='updatestateid'),
    path('sdelete/', views.sdelete, name='sdelete'),
                     #city
    path('savecity/', views.savecity, name='savecity'),
    path('updatecity/', views.updatecity, name='updatecity'),
    path('updatecityid/', views.updatecityid, name='updatecityid'),
    path('cdelete/', views.cdelete, name='cdelete'),

                     #cuisine
    path('cuisine/', views.openCusine, name='cuisine'),

    path('savecuisine/', views.savecuisine, name='savecuisine'),
    path('updatecuisine/', views.updatecuisine, name='updatecuisine'),
    path('updatecuisineid/', views.updatecuisineid, name='updatecuisineid'),
    path('dcuisine/', views.dcuisine, name='dcuisine'),


    path('logout/',views.login_check,name='logout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)