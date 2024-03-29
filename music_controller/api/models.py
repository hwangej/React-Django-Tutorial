import json
import random
import string

from django.db import models

# class BlogPost(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     published_date = models.DateTimeField(auto_now_add=True)


# class Userprofile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField()


# class Comment(models.Model):
#     post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
#     text = models.TextField()


# class Tag(models.Model):
#     name = models.CharField(max_length=30)
#     posts = models.ManyToManyField(BlogPost)


# # ORM을 사용하는 예제 코드
# class Author(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()

#     def __str__(self):
#         return self.name


# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     author = models.ForeignKey(Author, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.title


# def generate_unique_code():
#     length = 6
#     while True:
#         code = "".join(random.choices(string.ascii_uppercase, k=length))
#         if Room.objects.filter(code=code).count() == 0:
#             break

#     return code


# # Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)


# class Task(models.Model):
#     taskID = models.CharField(max_length=10, null=False)
#     taskName = models.CharField(max_length=50, null=False)
#     createDate = models.DateTimeField(max_length=50, null=False)
#     modifiedDate = models.DateTimeField(max_length=50, null=False)


# # # 설정다시
class QueueItems(models.Model):
    taskID = models.CharField(max_length=10, null=False)
    taskName = models.CharField(max_length=30, null=False)
    processName = models.CharField(max_length=50, null=False)
    queueName = models.CharField(max_length=50, null=False)
    machineName = models.CharField(max_length=15, null=False)
    jobKey = models.CharField(max_length=50, null=False)
    reference = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=50, null=False)
    exceptionType = models.CharField(max_length=50, null=False)
    date = models.CharField(max_length=50, null=False)
    createDtime = models.DateTimeField(auto_now_add=True)
    startDtime = models.DateTimeField(null=True)
    endDtime = models.DateTimeField(null=True)
    exceutionTime = models.TimeField(null=True)


# class Process:
#     # taskID = models.CharField(max_length=10, null=False)
#     path = "C:\\Users\\hyundai\\Documents\\React-Django-Tutorial\\music_controller\\process_queueItem_data.json"
#     with open(path, "r", encoding="UTF8") as file:
#         datas = json.load(file)

#     queue_item_list = []
#     for data in datas:
#         if data["STATUS"] == "Successful" or data["STATUS"] == "Failed":
#             task = data["TASK ID"]
#             process = data["QUEUE NAME"][6:15]
#         if data["HOST MACHINE NAME"] == None:
#             queue_item_list.append(
#                 QueueItems(
#                     task=task,
#                     process=process,
#                     queue_name=data["QUEUE NAME"],
#                     host_machine_name=data["HOST MACHINE NAME"],
#                     status=data["STATUS"],
#                     exception_type=data["EXCEPTION TYPE"],
#                     item_created_dtime=data["CREATE DTIME"],
#                     item_started_dtime=data["START DTIME"],
#                     item_ended_dtime=data["END DTIME"],
#                     item_execution_time=data["EXECUTION TIME"],
#                 )
#             )
#     QueueItems.objects.bulk_create(queue_item_list)
