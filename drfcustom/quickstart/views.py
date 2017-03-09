from django.contrib.auth.models import User, Group

from rest_framework import viewsets

from .serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

    # NB class attribute
    extra_bit = "thing"

    def __init__(self, **kwargs):
        super(UserViewSet, self).__init__(**kwargs)

        # instance attribute
        self.more = "more"


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
