from django.urls import path

from .views import QueueItemView, RoomView

urlpatterns = [
    path("room/", RoomView.as_view()),
    path("queueitems/", QueueItemView.as_view(), name="queue_item_list"),
]
