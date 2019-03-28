from stuapp.models import Actor, Movie
from rest_framework.viewsets import ModelViewSet
from stuapp.serializers import ActorSerializer, MovieSerializer

class ActorListView(ModelViewSet):
    """
     create:
     增加演员信息
     retrieve：
     查询某个演员详细信息
     update：
     更新某个演员信息
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieListView(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# from rest_framework.generics import
