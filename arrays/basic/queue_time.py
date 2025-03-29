"""
You need to calculate the total time required for all customers to check out at the self-checkout tills. 
You are given a sequence of times each customer takes to check out, along with the number of tills available.

In the input, you are given:
A series of positive integers where each integer represents the time a customer needs to check out.
A positive integer representing the number of tills available.

The output should be a single integer, which is the total time required for all customers to finish checking out.

To solve this, keep in mind:
There is one queue of customers that is served by multiple tills.
Customers are served in the order they are in line and assigned to tills as they become free.
The first customer goes to the first available till, and subsequent customers are assigned based on the time it 
takes for the tills to become free.

URL: https://www.codewars.com/kata/57b06f90e298a7b53d000a86
"""






def queue_time(customers: list[int], n: int) -> int:
    """
    Calcula el tiempo total necesario para que todos los clientes terminen de pagar en las cajas de autoservicio.

    Args:
        customers (list[int]): Lista con los tiempos de pago de cada cliente.
        n (int): Número de cajas disponibles.

    Returns:
        int: Tiempo total para que todos los clientes sean atendidos.
    """
    # Si no hay clientes, el tiempo total es 0
    if not customers:
        return 0
    
    # Inicializamos una lista con `n` cajas, todas comenzando en 0 segundos
    tills = [0] * n
    
    # Asignamos a cada cliente el tiempo de la caja con menor espera
    for time in customers:
        # Encontramos la caja con el menor tiempo acumulado y le sumamos el tiempo del nuevo cliente
        tills[0] += time
        # Reordenamos la lista para que la caja con menor tiempo acumulado vuelva a estar al inicio
        tills.sort()
    
    # El tiempo total será el tiempo máximo en alguna caja
    return max(tills)


print(queue_time([], 1))  # 0 (No hay clientes)
print(queue_time([5], 1))  # 5 (Un solo cliente en una caja)
print(queue_time([2, 3, 10], 2))  # 10 (El cliente con 10 ocupa toda una caja)
print(queue_time([2, 2, 3, 3, 4, 4], 2))  # 9 (Distribución equitativa)
print(queue_time([1, 2, 3, 4, 5], 100))  # 5 (Muchas cajas, cada cliente en una)
