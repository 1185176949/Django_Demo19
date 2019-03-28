import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
# Create your views here.
from django.views import View
from stuapp.models import Actor


class ActorListView(View):
    def get(self,request):
        """
        GET  /actors/
         查询所有演员信息
         """

        actors = Actor.objects.all()

        actorList = []

        for actor in actors:
            actorList.append({
                'aid':actor.aid,
                'aname':actor.aname,
                'age':actor.age,
                'agender':actor.agender,
                'birth_date':actor.birth_date,
                'photo':actor.photo.url if actor.photo else ''
            })
        return JsonResponse(actorList,safe=False)


    def post(self,request):
        """
        POST  /actors/
        新增一名演员信息

        :param request:
        :return:
        """
        #接收请求参数

        # b'aid=1&aname=zhangsan'
        bytes_str = request.body
        # 'aid=1&aname=zhangsan'
        str1 = bytes_str.decode()
        # {'aid':'1','aname':'zhangsan'}
        actor_dict = json.loads(str1)
        print(actor_dict)

        #省略请求参数的校验

        #将请求参数存入数据库
        #Actor.objects.create(aname='zhangsan',age='1',...)
        actor = Actor.objects.create(aname = actor_dict.get('aname'),age = actor_dict.get('age'),agender = actor_dict.get('agender'),birth_date = actor_dict.get('birth_date'))

        return JsonResponse({
                'aid':actor.aid,
                'aname':actor.aname,
                'age':actor.age,
                'agender':actor.agender,
                'birth_date':actor.birth_date,
                'photo':actor.photo.url if actor.photo else ''

            },status=201)

class ActorDetailView(View):
    def get(self,request,pk):
        """
        GET /actors/1/
        查看某个演员详情信息

        :param request:
        :param pk:
        :return:
        """
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        return JsonResponse({
                'aid':actor.aid,
                'aname':actor.aname,
                'age':actor.age,
                'agender':actor.agender,
                'birth_date':actor.birth_date,
                'photo':actor.photo.url if actor.photo else ''

            })

    def put(self,request,pk):

        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)


        #接收请求参数
        # b'aid=1&aname=zhangsan'
        bytes_str = request.body
        # 'aid=1&aname=zhangsan'
        str1 = bytes_str.decode()
        # {'aid':'1','aname':'zhangsan'}
        actor_dict = json.loads(str1)
        print(actor_dict)


        #校验过程省略

        actor.aname = actor_dict.get('aname')
        actor.age = actor_dict.get('age')
        actor.save()


        return JsonResponse({
                'aid':actor.aid,
                'aname':actor.aname,
                'age':actor.age,
                'agender':actor.agender,
                'birth_date':actor.birth_date,
                'photo':actor.photo.url if actor.photo else ''

            })

    def delete(self,request,pk):
        try:
            actor = Actor.objects.get(aid=pk)
        except Actor.DoesNotExist:
            return HttpResponse(status=404)

        actor.delete()


        return JsonResponse({'message':'OK'})