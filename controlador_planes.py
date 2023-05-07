from plan_ahorro import PlanAhorro
import csv
import os

class ControladorPlanes:
    
    def __init__(self):
        self.__planes = []
        
    def cargar_plan(self, plan):
        self.__planes.append(plan)
        
    def modifica_valor(self):
        for plan in self.__planes:
            print('Codigo: {}'.format(plan.get_cod()))
            print('Modelo:' + plan.get_modelo())
            print('Version del Vehiculo: ' + plan.get_version())
            print('')
            plan.modificar_valor()
    
    def mostrar_datos(self):
        valor = float(input('Ingrese el valor de Cuota:'))
        for plan in self.__planes:
            if plan.calculo_cuota() < valor:
                print('Codigo: {}'.format(plan.get_cod()))
                print('Modelo:' + plan.get_modelo())
                print('Version del Vehiculo: ' + plan.get_version())
                print('')
                
    def mostrar_valor_licitar(self):
        for plan in self.__planes:
            print('Codigo: {}'.format(plan.get_cod()))
            print('Modelo:' + plan.get_modelo())
            print('Version del Vehiculo: ' + plan.get_version())
            print('${}'.format(plan.calculo_cuota_licitar()))
            print('')
            
    def test_planes(self):
        ruta_archivo = os.path.abspath('planes.csv')
        if os.path.exists(ruta_archivo):
            archivo = open(ruta_archivo)
            reader = csv.reader(archivo, delimiter=';')
            for fila in reader:
                unPlan = PlanAhorro(int(fila[0]), fila[1], fila[2], float(fila[3]))
                self.cargar_plan(unPlan)
        else:
            print('El archivo no existe en la ruta de acceso especificada.')

    def get_plan(self, indice)->PlanAhorro:
        return self.__planes[indice]
            
    def buscar_plan(self, cod):
        i=0
        flag = False
        while not flag and i < len(self.__planes):
            if self.__planes[i].get_cod() == cod:
                flag = True
            else:
                i+=1
            return i
        
    def modificar_cantidad_cuotas(self):
        cuotas = int(input('Ingrese la nueva cantidad de cuotas para licitar'))
        cod = int(input('Ingrese el codigo del plan a modificar las cuotas para licitar'))
        num = self.buscar_plan(cod)
        if num <= len(self.__planes):
            Plan = self.get_plan(num)
            Plan.modificar_cuotas_licitar(cuotas)
        else:
            print('El plan no se encontró')