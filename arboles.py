## clase que genera el arbol
class Arbol:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = str(data)

    # Insertar un nodo en el árbol
    def insertar(self, data):
        data = str(data)
        if data < self.data:
            if self.left is None:
                self.left = Arbol(data)
            else:
                self.left.insertar(data)
        elif data > self.data:
            if self.right is None:
                self.right = Arbol(data)
            else:
                self.right.insertar(data)

    # Recorrido preorden: raíz → izquierda → derecha
    def preorden(self):
        result = [self.data]
        if self.left:
            result += self.left.preorden()
        if self.right:
            result += self.right.preorden()
        return result

    # Recorrido inorden: izquierda → raíz → derecha
    def inorden(self):
        result = []
        if self.left:
            result += self.left.inorden()
        result.append(self.data)
        if self.right:
            result += self.right.inorden()
        return result

    # Recorrido postorden: izquierda → derecha → raíz
    def postorden(self):
        result = []
        if self.left:
            result += self.left.postorden()
        if self.right:
            result += self.right.postorden()
        result.append(self.data)
        return result

# Crear raíz
raiz_usuario = input("Elige el nodo raíz: ")
root = Arbol(raiz_usuario)

# Bucle que le pregunta al usuario que secuencia quiere ingresar
while True:
    entrada = input("¿Quieres terminar el árbol? (yes) Si no, ingresa el valor: ")
    if entrada.lower() == "yes":
        break
    else:
        root.insertar(entrada)

# Muestra los 3 resultados
print("\nRecorridos del árbol:")
print("Preorden :", " ".join(root.preorden()))
print("Inorden  :", " ".join(root.inorden()))
print("Postorden:", " ".join(root.postorden()))
