# LISTA DOBLEMENTE ENLAZADA LINEAL
# Ejemplo: Lista de reproducción de canciones


# Clase Nodo
class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None


# Clase Lista Doblemente Enlazada
class ListaDoble:
    def __init__(self):
        self.inicio = None
        self.final = None

    # Agregar una canción
    def agregar(self, cancion):
        nuevo = Nodo(cancion)

        # Si la lista está vacía
        if self.inicio is None:
            self.inicio = nuevo
            self.final = nuevo

        # Si ya existen canciones
        else:
            nuevo.anterior = self.final
            self.final.siguiente = nuevo
            self.final = nuevo

    # Mostrar canciones de inicio a final
    def mostrar_adelante(self):
        if self.inicio is None:
            print("La playlist está vacía.")
            return

        actual = self.inicio

        print("\n--- PLAYLIST DE INICIO A FINAL ---")

        while actual is not None:
            print("🎵", actual.cancion)
            actual = actual.siguiente

    # Mostrar canciones de final a inicio
    def mostrar_atras(self):
        if self.final is None:
            print("La playlist está vacía.")
            return

        actual = self.final

        print("\n--- PLAYLIST DE FINAL A INICIO ---")

        while actual is not None:
            print("🎵", actual.cancion)
            actual = actual.anterior


# Crear la lista
playlist = ListaDoble()


# Agregar canciones
playlist.agregar("Despacito")
playlist.agregar("Blinding Lights")
playlist.agregar("Titi Me Preguntó")
playlist.agregar("Shape of You")
playlist.agregar("Hawái")


# Mostrar hacia adelante
playlist.mostrar_adelante()


# Mostrar hacia atrás
playlist.mostrar_atras()