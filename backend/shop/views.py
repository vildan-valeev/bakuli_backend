from django.core.mail import send_mail
from django.forms import ModelForm
from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, \
    DestroyAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Actual, Category, Store, CartItem, Cart, Order, Item
from .serializers import ActualSerializer, CategorySerializer, StoreSerializer, MenuSerializer, CartItemSerializer, \
    CartSerializer, OrderSerializer, ItemAdditionalSerializer, ItemDetailSerializer, \
    CartDetailSerializer, OrderCreateSerializer


# ----------------------   Category   ----------------------------
class CategoryList(ListAPIView):
    """Category list view"""
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


# ----------------------   Store   ----------------------------
class StoreList(ListAPIView):
    """Store list view"""
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


class StoreDetail(RetrieveAPIView):
    """Store detail view"""
    serializer_class = StoreSerializer
    queryset = Store.objects.all()


# ----------------------   Actual   ----------------------------
class ActualList(ListAPIView):
    """News, ads list"""
    serializer_class = ActualSerializer
    queryset = Actual.objects.all()


class ActualDetail(RetrieveAPIView):
    """Detail information of news"""
    serializer_class = ActualSerializer
    queryset = Actual.objects.all()


# ----------------------   Menu   ----------------------------
class MenuList(APIView):
    """
    Main menu list view- categories with nested item_group and items.
    .../menu/{id}/ - it's store id
    """
    def get(self, request, pk, format=None):
        queryset = Category.objects.all()
        serializer = MenuSerializer(instance=queryset, many=True, pk=pk)
        return Response(serializer.data)


# ----------------------   Item   ----------------------------
class ItemAdditionalList(APIView):
    """Additional Item list view, get by category id"""
    serializer_class = ItemAdditionalSerializer


    def get_object(self, pk):
        try:
            q = Item.objects.filter(category=pk, additional=True)
            print(q)
            return q
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print(pk)
        snippet = self.get_object(pk)
        serializer = ItemAdditionalSerializer(snippet, many=True)
        return Response(serializer.data)


class ItemDetail(RetrieveAPIView):
    """Item detail view"""
    serializer_class = ItemDetailSerializer
    queryset = Item.objects.all()


# ----------------------   CartItem   ----------------------------
class CartItemCreate(CreateAPIView):
    """ Create Cart Item.
    total_price можно не указывавть, расчитывается автоматически
    """
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated, ]
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()



class CartItemView(RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


# ----------------------    Cart   ----------------------------
class CartCreate(CreateAPIView):
    """ """
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    serializer_class = CartSerializer
    queryset = Cart.objects.all()



class CartDetail(RetrieveAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartDetailSerializer


class CartUpdateDelete(UpdateAPIView, DestroyAPIView):
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


# ----------------------    Order   ----------------------------
class OrderCreate(CreateAPIView):
    """ Можно использовать без авторизации"""
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = [IsAuthenticated]
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class OrderView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SendEmail(APIView):
    def get(self, request, format=None):
        send_mail(
            'ORDER FROM BAKULI',
            'Here is the message.',
            'from@example.com',
            ['onetmbot@gmail.com'],
            fail_silently=False,
        )
        return Response({'email': 'sended'})


