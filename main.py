from plan_ahorro import PlanAhorro
from controlador_planes import ControladorPlanes
from menu import Menu

if __name__ == '__main__':
    opciones = Menu()
    planes = ControladorPlanes()
    planes.test_planes()
    opciones.menu(planes)