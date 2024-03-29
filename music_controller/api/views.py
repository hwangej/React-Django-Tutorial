import json

from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import QueueItems, Room
from .serializers import QueueItemSerializer, RoomSerializer

# Create your views here.

# Model 데이터 가져오가 View에 넣어본다
class Process(generics.ListAPIView):
    # queryset = QueueItems.objects.all()
    serializer_class = QueueItemSerializer

    # @api_view(["GET"])
    def get_queryset(self):
        # taskID = models.CharField(max_length=10, null=False)
        path = "C:\\Users\\hyundai\\Documents\\React-Django-Tutorial\\music_controller\\process_queueItem_data.json"
        with open(path, "r", encoding="UTF8") as file:
            datas = json.load(file)
        queue_item_list = []
        for data in datas:
            if data["STATUS"] == "Successful" or data["STATUS"] == "Failed":
                task = data["TASK ID"]
                process = data["QUEUE NAME"][6:15]
            if data["HOST MACHINE NAME"] == None:
                queue_item_list.append(
                    QueueItems(
                        taskID=task,
                        taskName=data["TASK NAME"],
                        processName=process,
                        queueName=data["QUEUE NAME"],
                        machineName=data["HOST MACHINE NAME"],
                        jobKey=data["JOB KEY"],
                        reference=data["REFERENCE"],
                        status=data["STATUS"],
                        exception_type=data["EXCEPTION TYPE"],
                        date=data["DATE"],
                        createDtime=data["CREATE DTIME"],
                        startDtime=data["START DTIME"],
                        endDtime=data["END DTIME"],
                        exceutionTime=data["EXECUTION TIME"],
                    )
                )
        QueueItems.objects.bulk_create(queue_item_list)
        return queue_item_list


# addModelData = Process()
# addModelData.get_queryset()


class createRoom(generics.ListAPIView):
    serializer_class = RoomSerializer
    room_list = []

    def create_room(self):
        self.room_list.append(
            Room(
                code="ck019",
                host="hij3360",
                guest_can_pause=True,
                votes_to_skip=3,
                created_at="",
            )
        )

    Room.objects.bulk_create(room_list)


# 모든 다른 방을 반환하도록 설정된 뷰
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class QueueItemView(generics.ListAPIView):
    queryset = QueueItems.objects.all()
    serializer_class = QueueItemSerializer
