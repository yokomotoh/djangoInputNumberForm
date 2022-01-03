from django.urls import path

from . import views

#app_name = 'numberform'
#urlpatterns = [
#    path("<int:id>", views.index, name="index"),
#    path("", views.home, name="home"),
#    path("create/", views.create, name="create"),
#]

from . import forms

#from .views import HomeView
from .views import InputFormCreate

#app_name = 'numberform'
urlpatterns = [
    #path("inputform/", views.home_view, name="inputform"),
    #path("testnumber/", forms.TestNumberModel, name="testnumber"),
    #path('inputform/', HomeView.as_view(), name='testnumber-home'),
    path('createtestnumber/', InputFormCreate.as_view(), name='testnumber-create')
]

from .views import InputFormList
urlpatterns += [
    path('inputformlist/', InputFormList.as_view(), name='testnumber-list')
]

from .views import InputFormDetailView
urlpatterns += [
    path('<pk>/', InputFormDetailView.as_view(), name='testnumber-detail')
]

from .views import InputFormUpdateView
urlpatterns += [
    path('<pk>/update/', InputFormUpdateView.as_view(), name='testnumber-update')
]

from .views import InputFormDeleteView
urlpatterns += [
    path('<pk>/delete/', InputFormDeleteView.as_view(), name='testnumber-delete')
]

urlpatterns += [
    path('', views.index, name='index'),
]