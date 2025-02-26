"""
Given a year, return the century it is in.

URL: https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097
"""





def century(year: int) -> int:
    """
    Esta función recibe un año y retorna el siglo correspondiente.
    
    Args:
        year (int): El año del cual se determinará el siglo.
        
    Returns:
        int: El siglo correspondiente al año.
    """
    return (year + 99) // 100

test1 = century(18)
print(f"Siglo: {test1}")

test2 = century(2025)
print(f"Siglo: {test2}")
