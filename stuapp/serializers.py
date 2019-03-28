from rest_framework import serializers
from stuapp.models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    """演员序列化器"""
    class Meta:
        model = Actor
        fields = ('aname','age','agender')
        # 指明只读字段
        read_only_fields = ('mid',)

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
        # 嵌套
        depth = 1
        # 添加或修改原有的选项参数
        extra_kwargs = {
            'mread': {'min_value': 0, 'required': False},
            'mcomment': {'required': False}
        }