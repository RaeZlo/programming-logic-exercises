"""
A stream of data is received, and the order of its segments needs to be reversed.
Each segment is 8 bits (1 byte). We need to reverse the order of the segments, but not change the bits inside each segment.

URL: https://www.codewars.com/kata/569d488d61b812a0f7000015
"""





def data_reverse(data:list[int]) -> list[int]:
    """
    Reordena los segmentos de 8 bits en una secuencia de datos, sin modificar el contenido de los segmentos.

    Args:
        data (list[int]): Lista de bits (múltiplo de 8).

    Returns:
        list[int]: Lista de bits con los segmentos en orden invertido.
    """
    # Dividir los bits en segmentos de 8 bits (bytes)
    fragmented_bytes  = [data[i:i+8] for i in range(0, len(data), 8)]
    # Invertir el orden de los segmentos
    reversed_bytes = fragmented_bytes[::-1]
    # Aplanar la lista de segmentos invertidos en una sola lista de bits
    return [bit for byte in reversed_bytes for bit in byte]

def data_reverse_alt(data: list[int]) -> list[int]:
    """
    Alternativa para invertir los segmentos de 8 bits en la secuencia de datos.

    Args:
        data (list[int]): Lista de bits (múltiplo de 8).

    Returns:
        list[int]: Lista de bits con los segmentos en orden invertido.
    """
    res = []
    # Iteramos sobre la lista 'data' en pasos de 8 elementos, comenzando desde el final
    # 'len(data)-8' es el índice del primer segmento de 8 bits desde el final
    for i in range(len(data)-8, -1, -8):
        # Extraemos un segmento de 8 bits desde 'i' hasta 'i+8' (sin incluir el índice 'i+8')
        # Esto devuelve una lista con los 8 bits correspondientes
        res.extend(data[i:i+8])
    return res


print(data_reverse([1,1,1,1,0,0,0,0,  0,0,0,0,1,1,1,1]))  # [0,0,0,0,1,1,1,1,  1,1,1,1,0,0,0,0]
print(data_reverse([1,0,0,1,1,1,0,0,  0,1,1,0,1,0,0,1]))  # [0,1,1,0,1,0,0,1,  1,0,0,1,1,1,0,0]
print(data_reverse([0,0,1,1,1,1,0,0,  1,1,0,0,1,0,1,1]))  # [1,1,0,0,1,0,1,1,  0,0,1,1,1,1,0,0]
print(data_reverse([1,0,1,0,1,0,1,0,  0,1,0,1,0,1,0,1]))  # [0,1,0,1,0,1,0,1,  1,0,1,0,1,0,1,0]
