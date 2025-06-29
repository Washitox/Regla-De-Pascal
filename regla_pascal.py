class ReglaDePascal:
    def __init__(self):
        pass

    def calcular_combinacion(self, n, k):
        """
        Calcula el valor combinatorio (n k) usando la regla de Pascal recursivamente.
        Parámetros:
            n (int): número total de elementos
            k (int): número de elementos seleccionados
        Retorna:
            int: el valor de la combinación (n k)
        """

        # Condiciones base de la regla de Pascal
        if k == 0 or k == n:
            return 1
        else:
            # Regla de Pascal: C(n, k) = C(n-1, k-1) + C(n-1, k)
            return self.calcular_combinacion(n - 1, k - 1) + self.calcular_combinacion(n - 1, k)

# Ejemplo de uso del programa
if __name__ == "__main__":
    pascal = ReglaDePascal()

    
    n = 4
    k = 2
    resultado = pascal.calcular_combinacion(n, k)

    print(f"El valor de C({n}, {k}) es: {resultado}")
