from django.urls import path
from shop.views import ActualList, ActualDetail, MenuList, CategoryList, StoreList, OrderCreate, CartCreate, \
    CartItemCreate, CartItemView, OrderView, StoreDetail, ItemAdditionalList, ItemDetail, CartUpdateDelete, \
    CartDetail, SendEmail

urlpatterns = [

    path('active/', ActualList.as_view()),
    path('active/<int:pk>/', ActualDetail.as_view()),

    path('menu/<int:pk>/', MenuList.as_view()),

    path('category/', CategoryList.as_view()),

    path('items-additional/<int:pk>/', ItemAdditionalList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),

    path('store/', StoreList.as_view()),
    path('store/<int:pk>/', StoreDetail.as_view()),

    path('order/create/', OrderCreate.as_view()),
    path('order/<int:pk>/', OrderView.as_view()),

    path('cart/create/', CartCreate.as_view()),
    path('cart/detail/<int:pk>/', CartDetail.as_view()),
    path('cart/update-delete<int:pk>/', CartUpdateDelete.as_view()),

    path('cartitem/create/', CartItemCreate.as_view()),
    path('cartitem/<int:pk>/', CartItemView.as_view()),

    path('send_email/', SendEmail.as_view()),
]
