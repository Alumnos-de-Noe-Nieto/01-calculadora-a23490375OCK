"""
Nivel 3: Validación de repeticiones V/L/D.

Los símbolos V, L y D NO pueden repetirse.
Ejemplos válidos: V, L, D, MCMXCIV
Ejemplos inválidos: VV, LL, DD
"""

def validar_repeticiones_vld(cadena: str) -> bool:
    """
    Valida que los símbolos V, L y D no se repitan (máximo 1).

    Nivel 3: Análisis Sintáctico - Repeticiones de símbolos únicos

    💡 PISTA: Verifica si existen los patrones "VV", "LL", "DD"
    💡 PISTA: Si encuentras cualquier patrón de 2+ repeticiones, retorna False
    💡 PISTA: Recuerda: VV, LL, DD son INVÁLIDOS

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-2

    Returns:
        bool: True si no hay repeticiones de V/L/D, False en caso contrario

    Examples:
        >>> validar_repeticiones_vld("V")
        True
        >>> validar_repeticiones_vld("VV")
        False
        >>> validar_repeticiones_vld("MCMXCIV")
        True
        >>> validar_repeticiones_vld("LL")
        False
        >>> validar_repeticiones_vld("DD")
        False
    """
    return all(simbolo * 2 not in cadena for simbolo in 'VLD')
