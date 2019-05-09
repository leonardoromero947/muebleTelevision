from gpiozero import LED,Buzzer
from time import sleep
import switchs as SW
import posicion_mueble as POMU
import armado_mueble as ARMU
import memoria as MEM

class Motores(object):

    ### MOTORES
    memoria = MEM.Extra()
    pruebas = False
    motores_posicion_mueble = POMU.Posicion_Mueble()
    switch_motores = SW.Switch()
    armar = ARMU.Armado_mueble()
    mueble_cerrado = False
    mueble_abierto = False
    mueble_pruebas = False
    mueble_proceso = 0
    log_activo = False


    testigo = LED(14)
    buzzer = Buzzer(24)

    def ejecucion_inicial(self):
        if(self.switch_motores.status_accionador()):
            if(self.switch_motores.status_seguro()):
                print ("SEGURO ACTIVO IMPOSIBLE EJECUTAR MOVIMIENTO")
                self.buzzer.on()
                sleep(1)
                self.buzzer.off()
                sleep(1)
                self.buzzer.on()
                sleep(1)
                self.buzzer.off()
                return  False
            else:
                return True
        else:
            return False

    def valida_status_mueble(self):
        self.motores_posicion_mueble.log_activo(self.log_activo)
        self.memoria.leer_xml()
        if(self.memoria.proceso == 1):
            print("MUEBLE INICIALMENTE CERRADO")
            self.mueble_cerrado_proceso_abrir()
        if(self.memoria.proceso == 6):
            print("MUEBLE INICIALMENTE ABIERTO")
            self.mueble_abierto_proceso_cerrar()
        if(self.memoria.proceso != 6 and self.memoria.proceso != 1):
            print("ESTADO AUN NO PROGRAMADO")

    def mueble_cerrado_proceso_abrir(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble()
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(1)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            self.armar.poste1_abrir()
            status_mueble = self.valida_continuar()
        if (status_mueble == 3):
            self.armar.puerta1_abrir()
            status_mueble = self.valida_continuar()
        if (status_mueble == 4):
            self.armar.puerta1_guardar()
            status_mueble = self.valida_continuar()
        if (status_mueble == 6):
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE ABIERTO")


    def mueble_abierto_proceso_cerrar(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble()
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(2)
            self.error_fatal()
        if (status_mueble == 6):
            self.armar.puerta1_desplegar()
            status_mueble = self.valida_continuar()
        if (status_mueble == 4):
            self.armar.puerta1_cerrar()
            status_mueble = self.valida_continuar()
        if (status_mueble == 3):
            self.armar.poste1_cerrar()
            status_mueble = self.valida_continuar()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE CERRADO")

    def valida_continuar(self):
        numero_status = 0
        if self.pruebas:
            validacion = True
            while validacion:
                numero_status = self.motores_posicion_mueble.consultar_status_mueble()
                continuar = raw_input("La posicion del diagrama es correcta s/n?")
                if continuar in ('s', 'S'):
                    self.memoria.insertar_proceso_xml(numero_status)
                    break
                else:
                    validacion = True
            return numero_status
        else:
            numero_status = self.motores_posicion_mueble.consultar_status_mueble()
            self.memoria.insertar_proceso_xml(numero_status)
            return numero_status

    def error_fatal(self):
        print("PELIGRO POSICION INVALIDA")
        self.buzzer.on()
        sleep(1)
        self.buzzer.off()
        self.buzzer.on()
        sleep(1)
        self.buzzer.off()