import switchs as SW
import posicion_mueble as PM
import memoria as EX
import motores as MTR

class Ejecutor(object):

    motores = MTR.Motores()
    switch = SW.Switch()
    status_mueble = PM.Posicion_Mueble()
    vida = True
    extra = EX.Extra()


    def iniciar(self):
        self.xml_proceso()
        print("PRESIONA BOTON DE INICIO")
        while self.vida:
            if(self.motores.ejecucion_inicial()):
                self.motores.valida_status_mueble()
                self.vida = self.opcional()

    def xml_proceso(self):
        self.extra.leer_xml()
        #self.extra.insertar_estados_finales_xml(3)
        #self.extra.leer_xml()
        #self.extra.verificar_variables()
        self.status_mueble.instructivo_digital()
        self.preguntar_ejemplo()
        self.opcional_log_sensores()
        self.motores.mueble_abierto = self.extra.abierto
        self.motores.mueble_cerrado = self.extra.cerrado
        self.motores.mueble_pruebas = self.extra.pruebas
        self.motores.mueble_proceso = self.extra.proceso
        self.motores.pruebas = self.extra.pruebas

    def opcional(self):
        if self.extra.pruebas:
            continuar = raw_input("Ejecutar programa? S/N")
            if continuar in ('s', 'S'):
                return True
            else:
                print("Adios")
                return False
        else:
            return True


    def opcional_log_sensores(self):
        self.motores.log_activo = self.extra.log

    def preguntar_ejemplo(self):
        if self.extra.ejemplo:
            self.status_mueble.ejemplo_diagrama()