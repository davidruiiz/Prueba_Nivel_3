class nodoArbol:
    
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info

class Superheroe:
    
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return self.nombre
    
class ArbolDecision:
        
    def __init__(self, arbol_decision):
        self.arbol_decision = arbol_decision
    
    def asignar_superheroe(self):
        nodo_actual = self.arbol_decision

        while True:
            if isinstance(nodo_actual.info, Superheroe):
                return nodo_actual.info
            else:
                respuesta = input(f"{nodo_actual.info} (Sí/No): ")
                if respuesta.lower() == "sí" or respuesta.lower() == "si" or respuesta.lower() == "s" or respuesta.lower() == 1:
                    nodo_actual = nodo_actual.izq
                elif respuesta.lower() == "no" or respuesta.lower() == "n" or respuesta.lower() == 0:
                    nodo_actual = nodo_actual.der

# Crear superhéroes
iron_man = Superheroe("Iron Man", "Líder para planear misiones de defensa, genio y domina el manejo de tecnología avanzada")
hulk = Superheroe("The Incredible Hulk", "Excelente opción para misiones de destrucción")
khan = Superheroe("Khan", "Ideal para misiones intergalácticas en equipo")
thor = Superheroe("Thor", "Poder para destruir ejércitos completos")
cap_america = Superheroe("Captain América", "Supersoldado de ética incorruptible ideal para comandar misiones de defensa y de recuperación")
cap_marvel = Superheroe("Capitana Marvel", "Muy poderosa y puede viajar por las distintas galaxias")
ant_man = Superheroe("Ant-Man", "Excelente en misiones de recuperación donde sea necesario no ser detectado")
nick_fury = Superheroe("Nick Fury", "El propio Nick Fury es la opción más lógica para elegir la próxima acción y moverse rápidamente de un lugar a otro")
winter_soldier = Superheroe("The Winter Soldier", "Ideal para misiones de recuperación donde requiera infiltrarse con personas del lugar")

# Crear árbol de decisión
arbol_decision = nodoArbol("¿La misión es intergaláctica?")

arbol_decision.izq = nodoArbol("¿La misión es en equipo?")
arbol_decision.der = nodoArbol("¿La misión es de defensa?")

arbol_decision.izq.izq = nodoArbol("¿La misión es de recuperación?")
arbol_decision.izq.der = nodoArbol("¿La misión es de destrucción?")

arbol_decision.izq.izq.izq = nodoArbol("¿La misión requiere infiltrarse con personas del lugar?")
arbol_decision.izq.izq.der = nodoArbol("¿La misión requiere no ser detectado?")

