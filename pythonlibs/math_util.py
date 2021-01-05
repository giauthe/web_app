from decimal import Decimal, ROUND_HALF_UP


def sum_decimal(first, second, decimal_digits):
    result = Decimal(first) + Decimal(second)
    exponent = Decimal("%s" % pow(10, -Decimal(decimal_digits)))
    return result.quantize(Decimal(exponent), ROUND_HALF_UP)
