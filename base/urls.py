from django.urls import path,include
from base import views

urlpatterns = [
    path('', views.index,name='home' ),
    path('detail_poll/<id>', views.detail_poll,name='detail-poll' ),
    path('vote_poll/<pk>', views.vote,name='vote' ),
]
