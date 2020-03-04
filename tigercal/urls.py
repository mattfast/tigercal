from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('groupform', views.groupform, name='groupform'),
    path('groups', views.groups, name='groups'),

    path('publicevents', views.publicevents, name='publicevents'),
    path('events/<int:group_id>', views.events, name='events'),
]