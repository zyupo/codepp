from django.db import models

# Create your models here.

#告警管理-服务监控
class Server_info(models.Model):
    server_name = models.CharField(max_length=30,primary_key=True,verbose_name='检测服务名称')
    server_ip = models.CharField(max_length=60,verbose_name='检测服务IP')
    server_port = models.IntegerField(verbose_name='检测服务端口')
    server_status = models.IntegerField(verbose_name='检测状态')




