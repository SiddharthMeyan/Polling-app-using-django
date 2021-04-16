from django.urls import path,include
from base import views
from base.views import PollAdd

urlpatterns = [
    path('', views.index,name='home' ),
    path('detail_poll/<pk>', views.detail_poll,name='detail-poll' ),
    path('vote_poll/<pk>', views.vote,name='vote' ),
    path('polladd', PollAdd.as_view(),name='polladd' ),
]
