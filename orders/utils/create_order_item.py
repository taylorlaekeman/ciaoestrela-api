from orders.models import CustomCard, OrderItem, OrderType

def create_order_item(order, details):
    order_type = OrderType.objects.get(name=details.pop('order_type'))
    item = OrderItem.objects.create(
        order=order,
        order_type=order_type,
    )
    if order_type.name == 'custom card':
        return create_custom_card(item, details)
    else:
        return create_custom_card(item, details)


def create_custom_card(order_item, details):
    return CustomCard.objects.create(order_item=order_item, **details)
