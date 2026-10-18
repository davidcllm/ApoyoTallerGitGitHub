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

if __name__ == "__main__":
    print(" Calculadora de Ecuación Cuadrática (ax^2 + bx + c = 0) ")
    val_a = input("Ingresa el valor de a: ")
    val_b = input("Ingresa el valor de b: ")
    val_c = input("Ingresa el valor de c: ")
    
    resultado = resolver_cuadratica(val_a, val_b, val_c)
    print(f"\nResultado: {resultado}")