"""
Nivel 2: Validación de repeticiones I/X/C/M.

Los símbolos I, X, C y M pueden repetirse hasta 3 veces consecutivas.
Ejemplos válidos: III, XXX, CCC, MMM
Ejemplos inválidos: IIII, XXXX, CCCC, MMMM
"""

def validar_repeticiones_icxm(cadena: str) -> bool:
    """
    Valida que los símbolos I, X, C, M no se repitan más de 3 veces consecutivas.

    Nivel 2: Análisis Sintáctico - Repeticiones de símbolos repetibles

    💡 PISTA: Verifica si existen los patrones "IIII", "XXXX", "CCCC", "MMMM"
    💡 PISTA: Si encuentras cualquier patrón de 4+ repeticiones, retorna False
    💡 PISTA: Recuerda: IIII, XXXX, CCCC, MMMM son INVÁLIDOS

    Args:
        cadena (str): La cadena de números romanos validada en Nivel 1

    Returns:
        bool: True si no hay más de 3 repeticiones, False en caso contrario

    Examples:
        >>> validar_repeticiones_icxm("III")
        True
        >>> validar_repeticiones_icxm("IIII")
        False
        >>> validar_repeticiones_icxm("XIX")
        True
        >>> validar_repeticiones_icxm("XXXX")
        False
        >>> validar_repeticiones_icxm("MMMCMXCIV")
        True
        >>> validar_repeticiones_icxm("MMMM")
        False
    """
    return all(simbolo * 4 not in cadena for simbolo in 'IXCM')
