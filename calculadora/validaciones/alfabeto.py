"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    """
    Valida si todos los caracteres de la cadena pertenecen al alfabeto romano.

    💡 PISTA: Usa .strip() para eliminar espacios en blanco laterales
    💡 PISTA: Retorna False si la cadena está vacía después de eliminar espacios
    💡 PISTA: Recuerda: espacios en blanco laterales NO deben afectar la validación

    Args:
        cadena (str): La cadena a evaluar. Ej: "XIV"

    Returns:
        bool: True si la cadena es completamente válida, False en caso contrario.

    Examples:
        >>> validar_simbolos("XIV")
        True
        >>> validar_simbolos("MCMXCIV")
        True
        >>> validar_simbolos("ABCD")
        False
        >>> validar_simbolos("X-IV")
        False
        >>> validar_simbolos("")
        False
        >>> validar_simbolos("  XIV  ")
        True
    """
    cadena = cadena.strip()
    if not cadena:
        return False
    simbolos_validos = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    return all(c in simbolos_validos for c in cadena)
