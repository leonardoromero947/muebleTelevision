import switchs as SW
import posicion_mueble as PM


class Ejecutor(object):
    switch = SW.Switch()
    status_mueble = PM.Posicion_Mueble()
    vida = True

    def iniciar(self):
        self.status_mueble.instructivo_digital()
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
        continuar = raw_input("Mostrar log de botones individuales? S/N")
        if continuar in ('s','S'):
            self.status_mueble.log_activo(True)
        else:
            self.status_mueble.log_activo(False)