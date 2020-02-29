from orders.models import CustomCard, Order, OrderType


def get_order_info(order_id):
    order = Order.objects.get(id=order_id)
    custom_card_type = OrderType.objects.get(name="custom card")
    custom_cards = CustomCard.objects.filter(order_item__order__id=order_id)
    return {
        'contact': order.contact,
        'cost': len(custom_cards) * custom_card_type.cost,
        'destination': order.destination,
        'items': [{ 'ideas': card.ideas, 'paper': card.paper.name } for card in custom_cards]
    }
