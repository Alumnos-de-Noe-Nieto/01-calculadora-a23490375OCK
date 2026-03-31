"""
Nivel 5: Validación de restas válidas (Análisis Semántico).

Solamente 6 pares específicos de símbolos son permitidos para restar:
IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)

Ejemplos válidos: IV, IX, XL, XC, CD, CM, XIV (X + IV)
Ejemplos inválidos: IL (49), IC (99), XD (490), XM (990), VX (5), LC (50)
"""


def validar_restas(cadena: str) -> bool:
    """
    Valida que las restas (sustracciones) sean válidas.

    Nivel 5: Análisis Semántico - Restas válidas

    💡 PISTA: Para detectar una sustracción (valor actual < valor siguiente):
    💡 PISTA: Ejemplo: "IV" → I(1) < V(5) → par "IV" está en SUSTRACCIONES_VALIDAS → True
    💡 PISTA: Ejemplo: "IL" → I(1) < L(50) → par "IL" NO está en SUSTRACCIONES_VALIDAS → False
    💡 PISTA: Ejemplo: "XIV" → X >= I, luego I < V → par "IV" está en SUSTRACCIONES_VALIDAS → True
    💡 PISTA: Ejemplo: "IIX" → I repetido antes de IX → False

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-4

    Returns:
        bool: True si todas las restas son válidas, False en caso contrario

    Examples:
        >>> validar_restas("IV")
        True
        >>> validar_restas("IX")
        True
        >>> validar_restas("IL")
        False
        >>> validar_restas("IC")
        False
        >>> validar_restas("XIV")
        True
        >>> validar_restas("IIX")
        False
        >>> validar_restas("MCMXCIV")
        True
    """
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    i = 0
    while i < len(cadena) - 1:
        par = cadena[i:i+2]
        if valores[cadena[i]] < valores[cadena[i+1]]:
            if par not in sustracciones_validas:
                return False
            if i > 0 and cadena[i-1] == cadena[i]:
                return False
            i += 2
        else:
            i += 1
    return True
