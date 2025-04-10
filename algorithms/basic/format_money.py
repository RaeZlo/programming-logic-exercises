"""
You need to create a function that takes a float and formats it as a dollar amount with two decimal places.

For example:
39.99 should become $39.99
3 should become $3.00

URL: https://www.codewars.com/kata/55902c5eaa8069a5b4000083
"""





def format_money(amount: float) -> str:
    """
    Formatea un número como monto en dólares con dos decimales.

    Args:
        amount (float): Monto a formatear.

    Returns:
        str: Representación del monto en formato "$xx.xx".
    """
    return f"${amount:.2f}"


print(format_money(39.99))  # "$39.99"
print(format_money(3))      # "$3.00"
print(format_money(0))      # "$0.00"
print(format_money(4.1))    # "$4.10"
