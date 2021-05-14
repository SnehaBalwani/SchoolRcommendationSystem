from django.urls import path

from . import views

# from .views import AddPlaceView, ChangePlaceView, PlacesView


urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),
    path('login/', views.loginpage, name="login"),
    path('category/', views.category, name="category"),
    path('category/<str:gender_name>', views.category_gender, name="category_gender"),
    path('searchmap/', views.searchmap, name="searchmap"),
    path('school_page/<str:pk>', views.school_page, name="school_page"),
    path('search/', views.search, name="search"),
    path('search_results', views.SearchResultsView, name="search_results"),
    path('', views.autocomplete, name="autocomplete"),
    path('near_me', views.near_me, name="near_me"),
    path('register_school', views.register_school, name="register_school"),
    path('registered', views.registered, name="registered"),
    # url(r'^location/', include('location.urls')),
    # url(r'', include('social_auth.urls')),
    path('add_details', views.add_details, name="add_details"),
    # path('location', views.location, name="location"),
    # re_path("^$", AddPlaceView.as_view(), name="add"),
    # re_path("^places/(?P<pk>[0-9]+)/$", ChangePlaceView.as_view(), name="change"),
    # re_path("^index_location/$", PlacesView.as_view(), name="index_location"),

]
