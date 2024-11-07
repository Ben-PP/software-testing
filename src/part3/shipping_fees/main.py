def shipping_fee_by_weight(weight: float) -> float:
    """Calculate shipping fee based on weight

    Args:
        weight (float): weight of the items
    Returns:
        float: the shipping fee
    Raises:
        ValueError: If weight is negative
    """

    if weight < 0:
        raise ValueError(f"Weight must not be negative, got {weight}")

    if weight < 1:
        return 4.99
    elif weight < 5:
        return 9.99
    else:
        return 14.99


def calculate_shipping_fee(total_price: float, total_weight: float) -> float:
    """Calculate shipping fee based on total price and total weight

    Args:
        total_price (float): total price of the items
        total_weight (float): total weight of the items
    Returns:
        float: the shipping fee
    Raises:
        ValueError: If total_price or total_weight is negative
    """

    if total_price < 0:
        raise ValueError(f"Total price must not be negative, got {total_price}")

    if total_weight < 0:
        raise ValueError(f"Weight must not be negative, got {total_weight}")

    if total_price > 100:
        return 0
    elif total_price > 50:
        return round(shipping_fee_by_weight(total_weight) / 2, 1) - 0.01
    else:
        return shipping_fee_by_weight(total_weight)
