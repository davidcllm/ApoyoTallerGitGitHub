# Guía Práctica: Taller de Git y GitHub

## 1. Primer commit (Hello World)

**Objetivo:** Mostrar cómo inicializar y hacer el primer commit.

**Comandos sugeridos:**
```bash
git init
# Crear el archivo main.py
git add main.py
git commit -m "feat: hello world inicial"
```

**Código en `main.py`:**
```python
print("Hello World")
```

---

## 2. Rama, PR y Merge (Estructura base)

**Objetivo:** Enseñar a crear una rama, trabajar sin romper `main`, y hacer un Pull Request y Merge.

**Comandos sugeridos:**
```bash
git checkout -b feature/estructura-base
# Editar el archivo
git add main.py
git commit -m "feat: estructura base e inputs del usuario"
# git push origin feature/estructura-base (Si muestras el PR en GitHub)
git checkout main
git merge feature/estructura-base
```

**Código en `main.py` (Se reemplaza todo con esto):**
```python
def resolver_cuadratica(a_input, b_input, c_input):
    return "Lógica matemática pendiente..."

if __name__ == "__main__":
    print(" Calculadora de Ecuación Cuadrática (ax^2 + bx + c = 0) ")
    val_a = input("Ingresa el valor de a: ")
    val_b = input("Ingresa el valor de b: ")
    val_c = input("Ingresa el valor de c: ")
    
    resultado = resolver_cuadratica(val_a, val_b, val_c)
    print(f"\nResultado: {resultado}")
```

---

## 3. Escenario de Conflicto (Dos ramas distintas)

**Objetivo:** Mostrar qué pasa cuando dos desarrolladores tocan la misma parte del código y cómo resolverlo.

### Paso 3.1: Rama A (Validaciones)
A partir de `main`, se crea la primera rama.

**Comandos:**
```bash
git checkout -b feature/validaciones
# Editar archivo
git commit -am "feat: validacion de tipos y ecuacion lineal"
```

**Código en `main.py` (Modifica solo la función):**
```python
def resolver_cuadratica(a_input, b_input, c_input):
    try:
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
    except ValueError:
        return "Error: Los coeficientes deben ser valores numéricos."

    if a == 0:
        if b == 0:
            return "Error: No es una ecuación válida (a y b son 0)."
        else:
            x = -c / b
            return f"Es una ecuación lineal. Raíz: x = {x}"

    return "Lógica matemática pendiente..."
```

### Paso 3.2: Rama B (Lógica de raíces)
Regresar a `main` y crear la segunda rama, ignorando lo que hizo la Rama A.

**Comandos:**
```bash
git checkout main
git checkout -b feature/logica-raices
# Editar archivo
git commit -am "feat: calculo de discriminante y raices reales"
```

**Código en `main.py` (Modifica solo la función, pisando el código base):**
```python
def resolver_cuadratica(a_input, b_input, c_input):
    a = float(a_input)
    b = float(b_input)
    c = float(c_input)

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return f"Dos raíces reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una raíz real doble: x = {x}"
    else:
        return "Lógica de raíces complejas pendiente..."
```

### Paso 3.3: Provocar y Resolver el Conflicto
**Comandos:**
```bash
git checkout main
git merge feature/validaciones  # Esto funciona perfecto (Fast-forward)
git merge feature/logica-raices # CONFLICTO.
```

Aquí se le muestras al público el archivo con los marcadores `<<<<<<<` y `>>>>>>>`. 
**Resolución en vivo:** Borrar los marcadores y combinar ambos bloques para que la función quede así, luego haces `git add` y `git commit`:

**Código en `main.py` tras resolver el conflicto:**
```python
def resolver_cuadratica(a_input, b_input, c_input):
    try:
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
    except ValueError:
        return "Error: Los coeficientes deben ser valores numéricos."

    if a == 0:
        if b == 0:
            return "Error: No es una ecuación válida (a y b son 0)."
        else:
            x = -c / b
            return f"Es una ecuación lineal. Raíz: x = {x}"

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return f"Dos raíces reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una raíz real doble: x = {x}"
    else:
        return "Lógica de raíces complejas pendiente..."
```

---

## 4. El Bug y el Rollback

**Objetivo:** Introducir un error crítico, hacer commit, darse cuenta del error y usar Git para deshacerlo de forma segura.

### Paso 4.1: El "Mal" Commit (Bug)
Agregamos la librería `math` normal, que va a crashear si el discriminante es negativo (Raíz de un negativo = ValueError en `math`).

**Comandos:**
```bash
# Editar archivo agregando 'import math' arriba y la lógica mala abajo
git commit -am "feat: soporte para raices complejas"
```

**Modificaciones a `main.py`:**
```python
import math # AGREGAR ESTO AL INICIO DEL ARCHIVO

# ... (resto del código igual hasta el final de la función) ...

    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una raíz real doble: x = {x}"
    else:
        # BUG INTENCIONAL: math.sqrt no soporta negativos, el programa "crasheará"
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f"Dos raíces complejas: x1 = {x1}, x2 = {x2}"
```
*Tip: Ejecuta el programa e ingresa a=1, b=1, c=1 para que el público vea cómo el programa se rompe por el error.*

### Paso 4.2: El Rollback
**Comandos:**
```bash
git log --oneline # Muestras el hash del commit del bug
git revert <hash-del-commit>
# Se abrirá el editor para confirmar el mensaje de reversión. Guárdalo.
```
*Explicar que revertir es mejor que borrar el historial, porque mantiene registro de lo que pasó y deshace los cambios creando un nuevo commit inverso.*

### Paso 4.3: La solución final (El código bueno)
Ahora sí, implementamos `cmath` para números complejos.

**Comandos:**
```bash
# Editar con la solución final correcta
git commit -am "fix: manejo correcto de raices complejas con cmath"
```

**Código Final Completo en `main.py`:**
```python
import cmath

def resolver_cuadratica(a_input, b_input, c_input):
    try:
        a = float(a_input)
        b = float(b_input)
        c = float(c_input)
    except ValueError:
        return "Error: Los coeficientes deben ser valores numéricos."

    if a == 0:
        if b == 0:
            return "Error: No es una ecuación válida (a y b son 0)."
        else:
            x = -c / b
            return f"Es una ecuación lineal. Raíz: x = {x}"

    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        return f"Dos raíces reales: x1 = {x1}, x2 = {x2}"
    elif discriminante == 0:
        x = -b / (2*a)
        return f"Una raíz real doble: x = {x}"
    else:
        # Uso de cmath para manejar raíces cuadradas de números negativos
        x1 = (-b + cmath.sqrt(discriminante)) / (2*a)
        x2 = (-b - cmath.sqrt(discriminante)) / (2*a)
        return f"Dos raíces complejas: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    print(" Calculadora de Ecuación Cuadrática (ax^2 + bx + c = 0) ")
    val_a = input("Ingresa el valor de a: ")
    val_b = input("Ingresa el valor de b: ")
    val_c = input("Ingresa el valor de c: ")
    
    resultado = resolver_cuadratica(val_a, val_b, val_c)
    print(f"\nResultado: {resultado}")
```
