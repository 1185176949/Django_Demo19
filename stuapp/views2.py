from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from stuapp.models import Actor
from stuapp.serializers import ActorSerializer, MovieSerializer

class ActorListView(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    """
    查询所有演员信息
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return MovieSerializer
        else:
            return ActorSerializer

    def latest(self, request):
        """
        返回最新出道的演员
        """
        actor = Actor.objects.latest('aid')
        serializer = self.get_serializer(actor)
        return Response(serializer.data)

    def age(self, request, pk):
        """
        修改演员的年龄
        """
        actor = self.get_object()
        actor.age = request.data.get('age')
        actor.save()
        serializer = self.get_serializer(actor)
        return Response(serializer.data)
