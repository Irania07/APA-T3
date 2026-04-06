"""
Módulo de Álgebra Lineal: Clase Vector
Irania Aguinaga Muñoz

Este módulo implementa operaciones avanzadas con vectores como el producto
de Hadamard, el producto escalar y la descomposición ortogonal.
"""

class Vector:
    def __init__(self, elementos):
        """
        Inicializa un objeto Vector.
        Argumentos: elementos (list) -> Lista de componentes numéricas.
        """
        self.elementos = [float(x) for x in elementos]

    def __repr__(self):
        """Representación legible del vector."""
        return f"Vector({self.elementos})"

    def __mul__(self, other):
        """
        Sobrecarga del operador *. Implementa el producto de Hadamard 
        (elemento a elemento) o la multiplicación por un escalar.
        
        Tests Unitarios:
        >>> v1 = Vector([1, 2, 3])
        >>> v1 * 2
        Vector([2.0, 4.0, 6.0])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 * v2
        Vector([4.0, 10.0, 18.0])
        """
        if isinstance(other, (int, float)):
            return Vector([x * other for x in self.elementos])
        elif isinstance(other, Vector):
            return Vector([a * b for a, b in zip(self.elementos, other.elementos)])

    def __rmul__(self, other):
        """Permite la multiplicación escalar por la izquierda (k * v)."""
        return self.__mul__(other)

    def __matmul__(self, other):
        """
        Sobrecarga del operador @. Implementa el producto escalar.
        
        Tests Unitarios:
        >>> v1 = Vector([1, 2, 3])
        >>> v2 = Vector([4, 5, 6])
        >>> v1 @ v2
        32.0
        """
        return sum(a * b for a, b in zip(self.elementos, other.elementos))

    def __floordiv__(self, other):
        """
        Sobrecarga del operador //. Devuelve la componente paralela (v1 || v2).
        Fórmula: ((v1 · v2) / |v2|²) * v2
        
        Tests Unitarios:
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 // v2
        Vector([1.0, 2.0, 1.0])
        """
        denominador = other @ other
        if denominador == 0:
            raise ZeroDivisionError("No se puede proyectar sobre un vector nulo.")
        factor = (self @ other) / denominador
        return other * factor

    def __mod__(self, other):
        """
        Sobrecarga del operador %. Devuelve la componente normal (v1 ⊥ v2).
        Fórmula: v1 - v1_paralela
        
        Tests Unitarios:
        >>> v1 = Vector([2, 1, 2])
        >>> v2 = Vector([0.5, 1, 0.5])
        >>> v1 % v2
        Vector([1.0, -1.0, 1.0])
        """
        return Vector([a - b for a, b in zip(self.elementos, (self // other).elementos)])

if __name__ == "__main__":
    import doctest
    doctest.testmod() 