from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework as filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "retrieve":
            return UserDetailSerializer
        return self.serializer_class

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAuthenticated,)
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        new_user = serializer.save(is_active=True)
        new_user.set_password(new_user.password)
        super().perform_create(new_user)


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_fields = ("paid_course", "paid_lessons", "method")
    ordering_fields = ("date_payment",)

