import random
class Entrenamiento:
    def __init__(self, usuario):
        self.usuario = usuario
        self.historial = []
        self.xp = 0

    def sumar_xp(self):
        self.xp += 10

    def registrar_ejercicio(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return
        
        if len(self.historial) >= 10:
            print("Máximo de ejercicios alcanzado")
            return
        
        self.historial.append(valor)
        self.sumar_xp()
        print("Ejercicio registrado")

    def ver_historial(self):
        for v in self.historial:
            print(v)

    def total(self):
        return sum(self.historial)

    def promedio(self):
        if len(self.historial) == 0:
            return 0
        return self.total() / len(self.historial)

    def ver_perfil(self, detallado=True):
        if detallado:
            print(f"Usuario: {self.usuario}")
            print(f"XP: {self.xp}")
            print(f"Ejercicios: {len(self.historial)}")
        else:
            print(f"Usuario: {self.usuario}")
            print(f"XP: {self.xp}")
    
class Cardio(Entrenamiento):
    def sumar_xp(self):
        self.xp += 20
nombre = input("Ingrese nombre de usuario: ")
tipo = int(input("Tipo (1=Pesas, 2=Cardio): "))
if tipo == 1:
    entrenamiento = Entrenamiento(nombre)
else:
    entrenamiento = Cardio(nombre)

while True:
    print("\n1. Registrar ")
    print("2. Historial")
    print("3. Total")
    print("4. Promedio")
    print("5. Perfil")
    print("6. Terminar")

    opcion = int(input("Seleccione opción: "))

    if opcion == 1:
        valor = float(input("Ingrese valor: "))
        entrenamiento.registrar_ejercicio(valor)

    elif opcion == 2:
        entrenamiento.ver_historial()

    elif opcion == 3:
        print("Total:", entrenamiento.total())

    elif opcion == 4:
        print("Promedio:", entrenamiento.promedio())

    elif opcion == 5:
        det = int(input("Detallado (1=Sí, 0=No): "))
        entrenamiento.ver_perfil(det == 1)

    elif opcion == 6:
        frases = ["Sigue adelante","No te rindas","Disciplina supera motivación","Eres más fuerte de lo que crees" ]
        print(random.choice(frases))
        break
    