from rest_framework import routers, serializers, viewsets, filters
from django.contrib.auth.models import Group
import django_filters.rest_framework
from api.models import User

class UserSerializer(serializers.ModelSerializer):
    organization = serializers.StringRelatedField(many=False, read_only=True)
    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class GroupViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['name', 'email']
    filterset_fields = ['phone']
    serializer_class = UserSerializer

    def get_queryset(self):
        # I'm guessing there's a better way to filter by group
        if self.request.user.groups.filter(name="administrator") or self.request.user.groups.filter(name="viewer"):
            return User.objects.filter(organization=self.request.user.organization)
        else:
            return User.objects.get(email=self.request.user.email)


