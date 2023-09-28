from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name="index"),
    path('premium/', views.premium, name="premium"),
    path('archive/', views.archive, name="archive"),
    path('downloads/<str:slug>/<int:id>', views.downloads,name="downloads"),
    path('contacts/', views.contacts, name="contacts"),
]