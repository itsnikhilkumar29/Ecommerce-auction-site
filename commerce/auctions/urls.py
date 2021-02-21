from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createlisting",views.createlisting,name="createlisting"),
    path("viewlisting/<int:listingid>",views.viewlisting,name="viewlisting"),
    path("viewprofile",views.viewprofile,name="viewprofile"),
    path("mylistings",views.mylistings,name="mylistings"),
    path("mybids",views.mybids,name="mybids"),
    path("addcomment/<int:listingid>",views.addcomment,name='addcomment'),
    path("makewinner/<int:listingid>/<str:username>/<int:amount>",views.makewinner,name='makewinner'),
    path("mywinnings",views.mywinnings,name='mywinnings')
]
