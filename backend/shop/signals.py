from django.db.models.signals import m2m_changed, post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from shop.models import Cart, CartItem, Order


@receiver(m2m_changed, sender=Cart.cart_items.through)
def save_price(sender, **kwargs):
    instance = kwargs['instance']
    ls = ['post_remove', 'post_add']
    if kwargs['action'] in ls:
        total_values = instance.cart_items.values('total_price')
        instance.final_price = sum([i['total_price'] for i in total_values])
        instance.save()

    # TODO: oбновить цену в корзине если изменилась цена CartItem


@receiver(post_save, sender=CartItem)
def edit_cart_add_item(sender, **kwargs):
    instance = kwargs['instance']
    cart = Cart.objects.get(pk=instance.cart.pk)
    cart.cart_items.add(instance)


@receiver(post_delete, sender=CartItem)
def edit_cart_delete_item(sender, **kwargs):
    instance = kwargs['instance']
    cart = Cart.objects.get(pk=instance.cart.pk)
    cart.cart_items.remove(instance)


@receiver(post_save, sender=Cart)
def edit_cart_add_item(sender, instance, created, **kwargs):
    # print(kwargs)
    if created is False:
        # print('ok')
        count = instance.cart_items.filter(parent__isnull=True).count()
        # print(count)
        Cart.objects.filter(pk=instance.id).update(total_items=count)

    # print('сохранено', instance)


# TODO: переписать в celery task
@receiver(post_save, sender=Order)
def send_email(sender, instance, created, **kwargs):
    # print(kwargs)
    if created:
        # TODO: ОВЕРЯЕМ ЕСТЬ ЛИ ПОЧТА, и авторизован ли юзер
        email = instance.customer.email
        print(email)
        if instance.customer.email is not None:
            total = instance.cart.final_price
            cart_items = instance.cart.cart_items.all()
            items = ''
            for count, i in enumerate(cart_items, start=1):
                items += f'{count}. {i.item.title}\n' \
                         f'Count: {i.qty_item} \n' \
                         f'Price: {i.item.price} \n' \
                         f'Total: {i.total_price}\n\n'
            msg = f"Dear, Customer!\n" \
                  f"Your order: №{instance.id}\n\n" \
                  f"{items}\n" \
                  f"-----------\n" \
                  f"Total price: {total} \n\n" \
                  f"Our store is located on {instance.store.street} {instance.store.house_number}, {instance.store.city}\n\n" \
                  f"Thanks for choosing us!"
            send_mail(
                'Order from BAKULI',
                msg,
                'from@example.com',
                [email],
                fail_silently=False,
            )
