from django.db import models
from django.conf import settings
from users.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=255, )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class IngredientCategory(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    title = models.CharField(max_length=255, )
    category = models.ForeignKey(IngredientCategory, related_name='ingredients',
                                 on_delete=models.CASCADE, null=True, blank=True, default=None)
    is_replaceable = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=255, )
    category = models.ManyToManyField(Category, related_name='items')
    ingredients = models.ManyToManyField(Ingredient, related_name='ingredient_items', blank=True)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField(null=True, blank=True, )
    store = models.ManyToManyField('Store', related_name='store_items')
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    additional = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, )
    updated = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return self.title

    def get_categories(self):
        return ", ".join([p.name for p in self.category.all()])


class CartItem(models.Model):
    """
    """
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='related_item')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty_item = models.PositiveIntegerField(default=1)
    comment = models.CharField(max_length=255, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, )
    updated = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return f'CartItem {self.id}'

    def save(self, *args, **kwargs):
        self.total_price = self.qty_item * self.item.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    """

    """
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    cart_items = models.ManyToManyField(CartItem, blank=True, related_name='related_cart')
    total_items = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    in_order = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, )
    updated = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    """

    """
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    STATUS_CHOICES = (
        (STATUS_NEW, 'New order'),
        (STATUS_IN_PROGRESS, 'In progress order'),
        (STATUS_READY, 'Ready order'),
        (STATUS_COMPLETED, 'Completed order')
    )
    DEINE_TYPE_SELF = 'self'
    DEINE_TYPE_DELIVERY = 'delivery'

    DEINE_TYPE_CHOICES = (
        (DEINE_TYPE_SELF, 'Abholung'),
        (DEINE_TYPE_DELIVERY, 'Lieferung')
    )

    PAYMENT_GOOGLE_APPLEPAY = 'GooglePay/ApplePay'
    PAYMENT_PAYPAL = 'Paypal'
    # PAYMENT_APPLEPAY = 'ApplePay'
    PAYMENT_BARZAHLUNG = 'Barzahlung bei Abholung'
    PAYMENT_KARTENZAHLUNG = 'Kartenzahlung bei Abholung'

    PAYMENT_TYPE_CHOISE = (
        (PAYMENT_GOOGLE_APPLEPAY, 'GooglePay/ApplePay'),
        (PAYMENT_PAYPAL, 'Paypal'),
        # (PAYMENT_APPLEPAY, 'ApplePay'),
        (PAYMENT_BARZAHLUNG, 'Barzahlung bei Abholung'),
        (PAYMENT_KARTENZAHLUNG, 'Kartenzahlung bei Abholung')
    )
    customer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=STATUS_NEW)

    deine_type = models.CharField(max_length=100, choices=DEINE_TYPE_CHOICES, default=DEINE_TYPE_SELF)
    deine_city = models.CharField(max_length=50, null=True, blank=True)
    deine_street = models.CharField(max_length=50, null=True, blank=True)
    deine_house_number = models.PositiveIntegerField(null=True, blank=True)
    deine_address_index = models.PositiveIntegerField(null=True, blank=True)
    payment_type = models.CharField(max_length=100, choices=PAYMENT_TYPE_CHOISE, default=PAYMENT_KARTENZAHLUNG)
    comment = models.TextField(null=True, blank=True)
    store = models.ForeignKey('Store', on_delete=models.CASCADE)

    receipt_time = models.DateTimeField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, )
    updated = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return f'{self.id}'


class Store(models.Model):
    """

    """
    title = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    house_number = models.PositiveIntegerField()
    index = models.PositiveIntegerField()

    def __str__(self):
        return f'Store at: {self.street} {self.house_number}, {self.city}'


# TODO: перенести в отдельный App
class Actual(models.Model):
    """
    Posts, news and actions for customers
    """
    title = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    text = models.TextField(null=True)
    published = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=True, )
    updated = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return self.title
