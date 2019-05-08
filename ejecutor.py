import switchs as SW
import posicion_mueble as PM
import memoria as EX

class Ejecutor(object):
    switch = SW.Switch()
    status_mueble = PM.Posicion_Mueble()
    vida = True
    extra = EX.Extra()

    def iniciar(self):
        self.extra.leer_xml()
        self.extra.verificar_variables()
        self.status_mueble.instructivo_digital()
        self.preguntar_ejemplo()
        self.opcional_log_sensores()
        while self.vida:
            #self.switch.pruebaSwitchs()
            self.vida = self.opcional()
            if self.vida:
                self.status_mueble.consultar_status_mueble()


    def opcional(self):
        continuar = raw_input("Ejecutar programa? S/N")
        if continuar in ('s','S'):
            return True
        else:
            print("Adios")
            return False

    def opcional_log_sensores(self):
        self.status_mueble.log_activo(self.extra.log)

    def preguntar_ejemplo(self):
        if self.extra.ejemplo:
            self.status_mueble.ejemplo_diagrama()