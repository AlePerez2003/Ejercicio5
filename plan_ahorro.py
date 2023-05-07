class PlanAhorro:
    __codigo: int
    __modelo: str
    __version_vehiculo: str
    __valor_vehiculo: float
    __total_cuotas = 60
    __cuotas_licitar = 10
    
    def __init__(self, codigo = 0, modelo = '', version= '', valor = 0.0):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__version_vehiculo = version
        self.__valor_vehiculo = valor
        
    def modificar_valor(self):
        nuevo_valor = int(input('Introduzca el nuevo valor del vehiculo'))
        self.__valor_vehiculo = nuevo_valor
        
    def calculo_cuota(self):
        importe = float((self.__valor_vehiculo/self.__total_cuotas) + (self.__valor_vehiculo * 0.10))
        return importe
    
    def calculo_cuota_licitar(self):
        return self.__cuotas_licitar * self.calculo_cuota()

    def get_cod(self):
        return self.__codigo
    
    def get_modelo(self):
        return self.__modelo
    
    def get_version(self):
        return self.__version_vehiculo
    
    def get_plan(self):
        return PlanAhorro(self.__codigo, self.__modelo, self.__version_vehiculo, self.__valor_vehiculo)
    
    def modficar_cuotas_licitar(self, nuevo_valor: int)->None:
        self.__cuotas_licitar = nuevo_valor

    