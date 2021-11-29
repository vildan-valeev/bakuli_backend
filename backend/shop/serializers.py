from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer, EmailField, CharField

from .models import Actual, Order, Cart, CartItem, Item, Category, Store, Ingredient, IngredientCategory


class ActualSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Actual
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    """ """

    class Meta:
        model = Category
        fields = '__all__'


# ----------------------   Ingredient   ---------------------------

class IngredientSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Ingredient
        fields = '__all__'


# class IngredientDetailSerializer(ModelSerializer):
#     """ """
#
#     class Meta:
#         model = Ingredient
#         fields = '__all__'


# ----------------------   Item   ----------------------------
class ItemDetailSerializer(ModelSerializer):
    """ Item serializer"""
    ingredients = IngredientSerializer(
        many=True,
        read_only=True,

    )
    ingredients_replaceable = SerializerMethodField('get_ingredients', default=None)

    class Meta:
        model = Item
        fields = ['id', 'title', 'category', 'image', 'description', 'price', 'ingredients', 'ingredients_replaceable']

    def get_ingredients(self, *args, **kwargs):
        print(args, kwargs)
        categories_ing = IngredientCategory.objects.filter(ingredients__ingredient_items=1)
        result = Ingredient.objects.filter(is_replaceable=True, category__in=categories_ing)
        serializer = IngredientSerializer(instance=result, many=True)
        return serializer.data


class ItemSerializer(ModelSerializer):
    """ Item serializer"""

    class Meta:
        model = Item
        fields = '__all__'


class ItemAdditionalSerializer(ModelSerializer):
    """ Item serializer for menu"""

    class Meta:
        model = Item
        fields = ['id', 'title']


class CartItemSerializer(ModelSerializer):
    """ """

    class Meta:
        model = CartItem
        fields = '__all__'


class CartItemDetailCartSerializer(ModelSerializer):
    """ """
    item = SlugRelatedField(read_only=True, slug_field='title')

    class Meta:
        model = CartItem
        fields = '__all__'


class CartDetailSerializer(ModelSerializer):
    """ """
    cart_items = CartItemDetailCartSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        # fields = '__all__'
        fields = ('id', 'cart_items', 'total_items', 'final_price',)


class CartSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Order
        fields = '__all__'


class OrderCreateSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Order
        # TODO: write exclide
        fields = ['id', 'cart', 'customer', 'store', 'receipt_time', 'comment', 'payment_type', 'status', 'deine_type',
                  'deine_city', 'deine_street', 'deine_house_number',
                  'deine_address_index', ]


class StoreSerializer(ModelSerializer):
    """ """

    class Meta:
        model = Store
        fields = '__all__'


class ItemMenuSerializer(ModelSerializer):
    """ Item serializer for menu"""

    class Meta:
        model = Item
        fields = ['id', 'title', 'price']


class MenuSerializer(ModelSerializer):
    """ Category serializer with nested item_groups and items"""

    def __init__(self, **kwargs):
        kwargs.pop('pk', None)
        super().__init__(**kwargs)

    items = SerializerMethodField('get_items')

    class Meta:
        model = Category
        fields = ['id', 'name', 'items']

    def get_items(self, *args, **kwargs):
        pk = self._kwargs['pk']
        items = Item.objects.filter(additional=False, category=args[0], store=pk)
        serializer = ItemMenuSerializer(instance=items, many=True)
        return serializer.data
