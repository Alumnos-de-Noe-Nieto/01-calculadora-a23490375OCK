[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fRu_XUxI)
# Calculadora de Números Romanos - Práctica Unidad 1

Bienvenido a tu primer proyecto de **Lenguajes y Autómatas I**.

En esta práctica construirás una calculadora de números romanos que simula un **pipeline de compilación**. Al completar la práctica, habrás implementado todas las fases de un compilador real: análisis léxico, sintáctico, semántico, generación de código, parsing y orquestación.

---

## 🎯 Qué Construirás

La práctica se divide en **8 niveles**, cada uno representa una fase del pipeline de compilación:

| Nivel | Fase de Compilador | Función a Implementar | Archivo |
|--------|-------------------|---------------------|----------|
| Nivel 1 | Análisis Léxico - Alfabeto | `validar_simbolos()` | `validaciones/alfabeto.py` |
| Nivel 2 | Análisis Sintáctico I - Repeticiones I/X/C/M | `validar_repeticiones_icxm()` | `validaciones/repeticiones_icxm.py` |
| Nivel 3 | Análisis Sintáctico II - Repeticiones V/L/D | `validar_repeticiones_vld()` | `validaciones/repeticiones_vld.py` |
| Nivel 4 | Análisis Sintáctico III - Orden Descendente | `validar_orden_descendente()` | `validaciones/orden_descendente.py` |
| Nivel 5 | Análisis Semántico - Restas Válidas | `validar_restas()` | `validaciones/restas.py` |
| Nivel 6 | Generación de Código - Conversión | `romano_a_entero()` | `conversor.py` |
| Nivel 7 | Parsing - Expresiones | `evaluar_expresion()`, `tokenizar_expresion()`, `validar_estructura_tokens()` | `parser.py` |
| Nivel 8 | Orquestación - Pipeline Completo | `evaluar()` | `expresion.py` |

> **Nota:** Este proyecto no es solo una calculadora. Es un minicompilador que valida, transforma y procesa un lenguaje formal, exactamente como lo hacen los compiladores modernos.

---

## 🚀 Cómo Comenzar

### Requisitos Previos

- **Sistema Operativo:** Windows 11 (asumido en esta práctica)
- **Python:** Versión 3.14 o superior
- **Git:** Conocimiento básico de línea de comandos

> **Nota:** Esta práctica asume que ya sabes cómo operar Python y Git desde la línea de comandos. No se cubre la instalación de estas herramientas.

### ⚠️ Archivos Permitidos y Restringidos

Solo puedes modificar archivos dentro del directorio `calculadora/`. Cualquier intento de modificar otros archivos (como `tests/`, `docs/`, `.github/`, etc.) será **rechazado automáticamente** por GitHub al hacer push. Los tests y la documentación están protegidos para garantizar consistencia en la evaluación.

**Archivos que PUEDES modificar:**
- `calculadora/validaciones/alfabeto.py`
- `calculadora/validaciones/repeticiones_icxm.py`
- `calculadora/validaciones/repeticiones_vld.py`
- `calculadora/validaciones/orden_descendente.py`
- `calculadora/validaciones/restas.py`
- `calculadora/conversor.py`
- `calculadora/parser.py`
- `calculadora/expresion.py`

**Archivos que NO puedes modificar:**
- Todos los archivos en `tests/` (tests automáticos)
- Todos los archivos en `docs/` (documentación)
- Archivos de configuración (`.github/`, `ruff.toml`, `pyproject.toml`)
- Este archivo `README.md`

### Pasos Iniciales

1. **Clonar el repositorio** desde GitHub Classroom

2. **Instalar dependencias** (abrir PowerShell o CMD en la raíz del proyecto):
   ```bash
   pip install ruff pytest
   ```

3. **Verificar instalación**:
   ```bash
   pytest tests/ -v
   ```
   Deberías ver algo como: `0 passed, 0 failed, 0 errors` (inicialmente todas las funciones lanzarán `NotImplementedError`)

---

## 📂 Estructura del Proyecto

```
proyectos/2026-1-LYM-01-calculadora/
├── README.md                          # Este archivo
├── docs/
│   ├── NOTAS_DE_CLASE.pdf             # Teoría de la unidad (material del profesor)
│   ├── PRACTICA.md                    # Especificación completa de la práctica ⭐
│   ├── PRUEBAS.md                    # Guía para correr pruebas locales ⭐
│   └── GUIA_RUFF.md                  # Guía de calidad de código ⭐
├── calculadora/
│   ├── validaciones/                  # Niveles 1-5
│   ├── conversor.py                    # Nivel 6
│   ├── parser.py                      # Nivel 7
│   ├── expresion.py                   # Nivel 8
│   ├── cli.py                        # REPL interactivo (ya implementado)
│   └── error.py                     # Excepciones
├── tests/                            # Tests automáticos
└── ruff.toml                         # Configuración de ruff
```

---

## 📚 Documentación

Para completar esta práctica, debes consultar los siguientes documentos:

| Documento | Descripción | Cuando Usarlo |
|------------|-------------|----------------|
| **[docs/NOTAS_DE_CLASE.pdf](docs/NOTAS_DE_CLASE.pdf)** | Teoría de la unidad (material del profesor) | Antes de implementar cada nivel |
| **[docs/PRACTICA.md](docs/PRACTICA.md)** | Especificación completa de la práctica ⭐ | Siempre - referencia principal |
| **[docs/PRUEBAS.md](docs/PRUEBAS.md)** | Guía para correr pruebas locales ⭐ | Antes de cada commit |
| **[docs/GUIA_RUFF.md](docs/GUIA_RUFF.md)** | Guía de calidad de código ⭐ | Antes de cada commit |

> **⭐ Importante:** Los documentos marcados con ⭐ son esenciales para completar la práctica. Léelos cuidadosamente.

---

## 🧪 Evaluación

### Sistema de Calificación Automatizada

Tu calificación será asignada automáticamente por **GitHub Classroom** (GitHub Actions). El sistema de evaluación ejecuta:

1. **Pruebas de calidad (30 puntos):**
   - Ejecuta `ruff check calculadora/`
   - Verifica que el código cumpla con PEP 8 y estándares profesionales

2. **Pruebas funcionales (70 puntos):**
   - Ejecuta `pytest tests/`
   - Verifica que todas las 10 funciones implementadas pasen los tests

### 📊 Calificación de la Unidad

Este proyecto representa el **50% de la calificación de la Unidad 1**. El otro **50%** corresponde a las asistencias registradas por el profesor durante las sesiones de clase.

**Cálculo de ejemplo:**
- Proyecto completado al 100% (todas las pruebas funcionales + calidad de código) = **50 puntos**
- Asistencia al 100% durante la unidad = **50 puntos**
- **Calificación total de la unidad** = 50 + 50 = **100**

**Ejemplos de escenarios:**
- Proyecto: 35/50 (75% de pruebas funcionales pasaron) + Asistencia: 50/50 = **85**
- Proyecto: 50/50 (todas las pruebas pasaron) + Asistencia: 30/50 = **80**
- Proyecto: 0/50 (no se entregó o falló) + Asistencia: 50/50 = **50**

### ⚠️ Importante - Política de Calificaciones

1. **No hay redondeo:** Una calificación de **69** no sube a **70**. El sistema de calificaciones **NO redondea** valores.

2. **Evaluación por unidades:** El sistema **Ambar del TECNM** NO permite promediar calificaciones de diferentes unidades. La evaluación se realiza unidad por unidad.

3. **Reprobación de unidad:** Si repruebas una unidad (calificación < 70), repruebas **todo el curso**. No hay forma de compensar una unidad reprobada con calificaciones altas en otras unidades.

**Conclusión:** Asegúrate de:
- Completar este proyecto con la mayor calidad posible
- Asistir a todas las clases posibles
- Evitar llegar a la situación de 69 puntos (trabaja desde el inicio para asegurar al menos 70)

### Ejecutar Pruebas Localmente

Antes de hacer commit y push, ejecuta las pruebas localmente:

```bash
# Verificar calidad de código
ruff check calculadora/

# Ejecutar todas las pruebas
pytest tests/ -v

# Ejecutar pruebas de un nivel específico
pytest tests/test_nivel_1_alfabeto.py -v
pytest tests/test_nivel_2_repeticiones_icxm.py -v
# ... etc.
```

### Resultados Esperados

Un proyecto completado exitosamente debería mostrar:

```bash
======================== 82 passed in X.XXs =====================
```

- **82 passed**: Todos los tests funcionales pasaron

---

## ✅ Flujo de Trabajo Recomendado

### Por Nivel

1. **Leer la teoría** del nivel en `docs/NOTAS_DE_CLASE.pdf`
2. **Leer la especificación** en `docs/PRACTICA.md`
3. **Implementar la función** en el archivo correspondiente
4. **Correr pruebas** del nivel: `pytest tests/test_nivel_X*.py -v`
5. **Verificar calidad**: `ruff check calculadora/`
6. **Corregir errores** hasta que las pruebas pasen
7. **Commit**: `git add . && git commit -m "feat: completar nivel X"`
8. **Continuar al siguiente nivel**

### Antes de Entregar

1. Ejecutar todas las pruebas: `pytest tests/ -v`
2. Verificar calidad: `ruff check calculadora/`
3. Probar el CLI para pruebas manuales:
   ```bash
   python3 -m calculadora
   ```
4. Probar expresiones de ejemplo en el REPL:
   ```
   🏛 > XIV + LX
   Resultado: 74
   ```
5. Commit final con mensaje claro
6. Push a GitHub: `git push`

---

## 🎯 Ejemplo de Uso Final

Una vez completado el proyecto, podrás usar la calculadora:

```bash
# Ejecutar el REPL interactivo
python3 -m calculadora

# Ejemplos de uso en el REPL:
🏛 > XIV + LX
Resultado: 74

🏛 > X - V
Resultado: 5

🏛 > MMMCMXCIX + I
Resultado: 4000
```

O desde código Python:

```python
from calculadora.expresion import evaluar

# Evaluar una expresión completa
resultado = evaluar('XIV + LX')
print(resultado)  # 74 (14 + 60 = 74)
```

---

## 💡 Consejos Importantes

- **Lee los docstrings:** Cada función tiene un docstring detallado con pistas pedagógicas
- **Desarrolla en orden:** Completa cada nivel antes de pasar al siguiente. Cada nivel depende de los anteriores.
- **Prueba incrementalmente:** No esperes a completar todo para probar. Ejecuta los tests después de cada nivel.
- **Usa ruff:** Ejecuta `ruff check calculadora/` regularmente mientras programas
- **Revisa los tests:** Los archivos de pruebas en `tests/` muestran exactamente qué casos deben cubrir tus implementaciones.

---

## 🆘 Soporte

Si tienes dudas durante el desarrollo:

1. **Revisa los docstrings** de cada función (contienen pistas pedagógicas)
2. **Lee la especificación** en `docs/PRACTICA.md`
3. **Revisa los tests** correspondientes a tu nivel actual
4. **Consulta la teoría** en `docs/NOTAS_DE_CLASE.pdf`
5. **Lee la guía de pruebas** en `docs/PRUEBAS.md`
6. **Consulta la guía de ruff** en `docs/GUIA_RUFF.md`
7. **Pregunta en el foro** del curso como último recurso

---

## 📋 Checklist de Entrega

- [ ] Todos los niveles implementados (1-8)
- [ ] Todas las pruebas pasan: `pytest tests/ -v` (82 passed)
- [ ] Calidad de código correcta: `ruff check calculadora/` (All checks passed!)
- [ ] CLI funcional para pruebas manuales: `python3 -m calculadora`
- [ ] Commit con mensaje claro
- [ ] Push a GitHub Classroom
- [ ] Verificar resultado en GitHub Actions

---

## 📖 Licencia

Este proyecto es parte del curso "Lenguajes y Autómatas I" y está diseñado para uso educativo.

---

**¡Buena suerte y happy coding!** 🚀🐍🏛️
