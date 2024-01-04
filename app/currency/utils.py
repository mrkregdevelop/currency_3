from decimal import Decimal, ROUND_DOWN


def to_2_places_decimal(value: str) -> Decimal:
    return Decimal(value).quantize(Decimal('0.00'), rounding=ROUND_DOWN)
