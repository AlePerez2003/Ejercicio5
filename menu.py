from plan_ahorro import PlanAhorro
from controlador_planes import ControladorPlanes

class Menu:
    __cod: int
    
    def __init__(self, cod = 0):
        self.__cod = cod
        
    def mostrar_menu(self):
        print('Opción 1: Actualizar valor del vehículo de cada plan')
        print('Opción 2: Mostrar datos del Plan segun un valor de cuota')
        print('Opción 3: Mostrar monto que debe haber pagado para la licitación')
        print('Opción 4: dado el código de un plan modificar la cantidad de cuotas necesarias para licitar')
        print('Opción 0: terminar operación')
        
    def menu(self, planes):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el código'))
        while self.__cod != 0:
            if self.__cod == 1:
                planes.modifica_valor()
            elif self.__cod == 2:
                planes.mostrar_datos()
            elif self.__cod == 3:
                planes.mostrar_valor_licitar()
            elif self.__cod == 4:
                planes.modificar_cantidad_cuotas()
            self.mostrar_menu
            self.__cod = int(input('Ingrese el código'))