"""
Nivel 4: Validación de orden descendente.

Los símbolos deben ir en orden descendente de valor (izquierda a derecha).
Excepción: las 6 formas sustractivas válidas.
Ejemplos válidos: XVI, MDCLXVI, XIV (sustracción válida)
Ejemplos inválidos: IVX, IIV, VIV
"""

def validar_orden_descendente(cadena: str) -> bool:
    """
    Valida que los símbolos estén en orden descendente de valor (izquierda a derecha).

    Nivel 4: Análisis Sintáctico - Orden descendente

    💡 PISTA: Usa la constante VALORES con el valor numérico de cada símbolo
    💡 PISTA: Usa la constante SUSTRACCIONES_VALIDAS = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    💡 PISTA: Recorre la cadena con un índice `i` usando un while loop
    💡 PISTA: Si cadena[i:i+2] está en SUSTRACCIONES_VALIDAS:
    💡 PISTA:   - Verifica que no haya repeticiones antes (ej: IIV es inválido, cadena[i-1] == cadena[i])
    💡 PISTA:   - Verifica que el símbolo anterior sea mayor al valor sustraído
    💡 PISTA:   - Verifica que después de la sustracción, el orden descendente continúe
    💡 PISTA: Si no es sustracción, verifica VALORES[cadena[i]] >= VALORES[cadena[i+1]]
    💡 PISTA: Ejemplo: "XVI" → X(10) >= V(5) >= I(1) → True
    💡 PISTA: Ejemplo: "IVX" → I(1) < V(5), pero luego V(5) < X(10) → False
    💡 PISTA: Ejemplo: "IIV" → I repetido antes de IV → False
    💡 PISTA: Ejemplo: "MCMXCIV" → varias sustracciones válidas → True

    Args:
        cadena (str): La cadena de números romanos validada en Niveles 1-3

    Returns:
        bool: True si el orden es correcto, False en caso contrario

    Examples:
        >>> validar_orden_descendente("XVI")
        True
        >>> validar_orden_descendente("IVX")
        False
        >>> validar_orden_descendente("MCMXCIV")
        True
        >>> validar_orden_descendente("IIV")
        False
        >>> validar_orden_descendente("VIV")
        False
    """
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sustracciones_validas = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
    i = 0
    while i < len(cadena) - 1:
        par = cadena[i:i+2]
        if par in sustracciones_validas:
            if i > 0 and cadena[i - 1] == cadena[i]:
                return False
            valor_par = valores[cadena[i+1]] - valores[cadena[i]]
            if i + 2 < len(cadena) and valores[cadena[i+2]] > valor_par:
                return False
            i += 2
        else:
            if valores[cadena[i]] < valores[cadena[i+1]]:
                return False
            i += 1
    return True
