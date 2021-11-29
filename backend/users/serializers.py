from djoser.serializers import UserCreateSerializer
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, EmailField, CharField

from shop.models import Order
from users.models import UserProfile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class OrderHistorySerializer(ModelSerializer):
    """ """
    price = SerializerMethodField('get_price')

    class Meta:
        model = Order
        fields = ['created', 'price']

    def get_price(self, obj):
        return obj.cart.final_price


class ProfileDetailSerializer(ModelSerializer):
    history = SerializerMethodField('get_history')

    class Meta:
        model = UserProfile

        fields = '__all__'
        # fields = (
        #     'id', 'email', 'photo', 'first_name', 'last_name', 'phone', 'city', 'street', 'house_number',
        #     'address_index', 'company', 'history'
        # )

    def get_history(self, *args, **kwargs):
        instance = args[0]
        orders = Order.objects.filter(customer_id=instance.id)
        serializer = OrderHistorySerializer(instance=orders, many=True)
        return serializer.data
