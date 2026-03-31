"""
Nivel 8: Orquestación del Pipeline Completo
Este módulo contiene la función principal para evaluar expresiones aritméticas de números romanos.
"""

from calculadora.conversor import romano_a_entero
from calculadora.error import ExpresionInvalida
from calculadora.parser import evaluar_expresion as parsear_expresion


def evaluar(expresion: str) -> int:
    """
    Pipeline completo - Orquestación de todos los niveles.

    Nivel 8: Integrar todo el pipeline de análisis léxico, sintáctico,
    semántico y parsing para evaluar expresiones aritméticas de números romanos.

    Pipeline de compilación:
    1. Análisis Léxico (Nivel 1): Validar alfabeto
    2. Análisis Sintáctico 1 (Nivel 2): Validar repeticiones I/X/C/M
    3. Análisis Sintáctico 2 (Nivel 3): Validar repeticiones V/L/D
    4. Análisis Sintáctico 3 (Nivel 4): Validar orden descendente
    5. Análisis Semántico (Nivel 5): Validar restas válidas
    6. Generación de Código (Nivel 6): Conversión romano→entero
    7. Parsing (Nivel 7): Tokenización y evaluación de expresiones
    8. Orquestación (Nivel 8): Pipeline completo

    💡 PISTA PRIMERO: Llama a parsear_expresion(expresion) para obtener los tokens
    💡 PISTA: Filtra tokens de tipo 'ESPACIO'
    💡 PISTA: Recorre los tokens restantes y aplica las operaciones correspondientes
    💡 PISTA: Al final, valida que el resultado sea positivo (> 0)
    💡 PISTA: Si el resultado es <= 0, lanza ExpresionInvalida con mensaje descriptivo
    💡 PISTA Ejemplo "XIV + LX":
    💡 PISTA:   - Tokens: [ROMANO "XIV", SUMA "+", ROMANO "LX"]
    💡 PISTA:   - romano_a_entero("XIV") = 14 → resultado = 14
    💡 PISTA:   - romano_a_entero("LX") = 60 → resultado = 14 + 60 = 74
    💡 PISTA Ejemplo "X - V":
    💡 PISTA:   - Tokens: [ROMANO "X", RESTA "-", ROMANO "V"]
    💡 PISTA:   - romano_a_entero("X") = 10 → resultado = 10
    💡 PISTA:   - romano_a_entero("V") = 5 → resultado = 10 - 5 = 5
    💡 PISTA Ejemplo "V - X":
    💡 PISTA:   - Tokens: [ROMANO "V", RESTA "-", ROMANO "X"]
    💡 PISTA:   - resultado = 5 - 10 = -5 → lanza ExpresionInvalida


    Args:
        expresion (str): La expresión aritmética a evaluar

    Returns:
        int: El resultado de la expresión

    Raises:
        ExpresionInvalida: Si la expresión tiene errores léxicos, sintácticos o semánticos
        ExpresionInvalida: Si el resultado de la expresión es negativo o cero

    Examples:
        >>> evaluar('XIV + LX')
        74
        >>> evaluar('X - V')
        5
        >>> evaluar('MMMCMXCIX + I')
        4000
    """
    tokens = parsear_expresion(expresion)
    if not tokens:
        raise ExpresionInvalida(f'La expresión "{expresion}" tiene una estructura inválida')
    tokens_sin_espacios = [t for t in tokens if t.tipo != 'ESPACIO']
    resultado = romano_a_entero(tokens_sin_espacios[0].valor)
    i = 1
    while i < len(tokens_sin_espacios) - 1:
        operador = tokens_sin_espacios[i].tipo
        valor = romano_a_entero(tokens_sin_espacios[i + 1].valor)
        if operador == 'SUMA':
            resultado += valor
        elif operador == 'RESTA':
            resultado -= valor
        i += 2
    if resultado <= 0:
        raise ExpresionInvalida(f'El resultado de "{expresion}" es negativo o cero')
    return resultado
