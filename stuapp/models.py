from django.db import models

# Create your models here.
"""以一个演员可以出演多部影片为例    1 ：N """


class Actor(models.Model):
    GENDER_ID = (
        ('0','男'),
        ('1','女')
    )
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=30,help_text='请输入修改后的年龄')
    age = models.PositiveIntegerField()
    agender = models.CharField(max_length=1,choices=GENDER_ID)
    birth_date = models.DateField()
    photo = models.ImageField(default='',upload_to='actors/')

    def __str__(self):
        return self.aname

class Movie(models.Model):
    mid = models.AutoField(primary_key=True)
    mname = models.CharField(max_length=30)
    m_pub_date = models.DateField()
    mread = models.PositiveIntegerField(default=0)
    mcomment = models.TextField()
    mimage = models.ImageField(upload_to='movies/')
    actors = models.ForeignKey(Actor,on_delete=models.CASCADE)


    def __str__(self):
        return self.mname