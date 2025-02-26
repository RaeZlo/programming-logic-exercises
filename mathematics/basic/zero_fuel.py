"""
You were camping with your friends far away from home, but when it's time to go back, you realize that 
your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs 
on about 25 miles per gallon. There are 2 gallons left.

Considering these factors, write a function that tells you if it is possible to get to the pump or not.
Function should return true if it is possible and false if not.

URL: https://www.codewars.com/kata/5861d28f124b35723e00005e
"""





def zero_fuel(distance_to_pump, mpg, fuel_left):
    """
    En esta función, verificamos si el vehículo tiene suficiente combustible 
    para llegar a la estación de servicio más cercana. Si la distancia a la estación 
    de servicio es menor o igual a la distancia que se puede recorrer con el combustible 
    disponible, entonces la función devolverá True. De lo contrario, devolverá False.
    
    Args:
        distance_to_pump (int): La distancia en millas hasta la estación de servicio.
        mpg (int): El rendimiento del vehículo en millas por galón.
        fuel_left (int): La cantidad de galones de combustible restantes.
        
    Returns:
        bool: True si es posible llegar a la estación de servicio, False en caso contrario.
    """
    return distance_to_pump <= mpg * fuel_left

# Pruebas de la función
test1 = zero_fuel(80, 25, 2)
print(f"¿Es posible llegar a la estación de servicio? {test1}")  # Esperado: True

test2 = zero_fuel(120, 25, 2)
print(f"¿Es posible llegar a la estación de servicio? {test2}")  # Esperado: False
