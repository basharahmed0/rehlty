from django.urls import path
from django.shortcuts import redirect

from . import views


urlpatterns = [path('signin/', views.signin_view, name='signin'),

 path('signup/', views.signup_view, name='signup'),   
   # path('', lambda request: redirect('signup')),
    path('book/', views.book_view, name='book'),
    path('home/', views.home_view, name='home'),
    path('details/', views.details_view, name='details'),
    path('payment/', views.payment_view, name='payment'),
    path('one/',views.one_view, name='one.html'),
    path('tow/',views.tow_view, name='tow.html'),
    path('three/',views.three_view, name='three.html'),
    path('four/',views.four_view, name='four.html'),
    path('aone/',views.aone_view, name='aone.html'),
    path('atow/',views.atow_view, name='atow.html'),
    path('athree',views.athree_view, name='athree.html'),
    path('afour/',views.afour_view, name='afour.html'),
    ]
      