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
        if(self.switch_motores.status_accionador() or self.switch_motores.status_accionador_control()):
            if(self.switch_motores.status_seguro()):
                print ("SEGURO ACTIVO IMPOSIBLE EJECUTAR MOVIMIENTO")
                self.buzzer.on()
                sleep(1)
                self.buzzer.off()
                sleep(1)
                self.buzzer.on()
                sleep(1)
                self.buzzer.off()
                return False
            else:
                return True
        else:
            return False

    def valida_status_mueble(self):
        self.motores_posicion_mueble.log_activo(self.log_activo)
        self.memoria.leer_xml()
        if(self.memoria.abierto is True or self.memoria.proceso == 1):
            print("MUEBLE INICIALMENTE CERRADO")
            self.mueble_cerrado_proceso_abrir()
        else:
            if(self.memoria.cerrado is True or self.memoria.proceso == 6 or self.memoria.proceso == 7 or self.memoria.proceso == 14 ):
                print("MUEBLE INICIALMENTE ABIERTO")
                self.mueble_abierto_proceso_cerrar()


    def mueble_cerrado_proceso_abrir(self):
        self.abrir_mueble_completo()

    def mueble_abierto_proceso_cerrar(self):
        self.cerrar_mueble_completo()

    def abrir_solo_puerta_a(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("A")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            self.armar.poste1_abrir(False)
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 3):
            self.armar.puerta1_abrir(False)
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 4):
            self.armar.puerta1_guardar(False)
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 6):
            status_mueble = self.valida_continuar("A")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE ABIERTO LADO A")

    def abrir_solo_puerta_b(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("B")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            status_mueble = self.valida_continuar("B")
            self.armar.poste2_abrir(False)
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 3):
            self.armar.puerta2_abrir(False)
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 5):
            self.armar.puerta2_guardar(False)
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 7):
            status_mueble = self.valida_continuar("B")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE ABIERTO LADO B")

    def abrir_mueble_completo(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("C")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(1)
            self.error_fatal()
        if (status_mueble == 1):
            self.memoria.insertar_estados_finales_xml(1)
            self.armar.poste1_abrir(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 2):
            self.memoria.insertar_estados_finales_xml(1)
            self.armar.poste1_abrir(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 3):
            self.armar.poste2_abrir(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 4):
            self.armar.poste2_abrir(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 5):
            self.armar.puerta1_abrir(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 6):
            self.armar.puerta1_abrir(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 7):
            self.armar.puerta2_abrir(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 8):
            self.armar.puerta2_abrir(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 9):
            self.armar.puerta1_guardar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 10):
            self.armar.puerta1_guardar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 11):
            self.armar.puerta2_guardar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 12):
            self.armar.puerta2_guardar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 14):
            status_mueble = self.valida_continuar("C")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE COMPLETAMENTE ABIERTO")

    def cerrar_solo_puerta_a(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("A")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 6):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta1_desplegar(False)
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 4):
            self.armar.puerta1_cerrar(False)
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 3):
            self.armar.poste1_cerrar(False)
            status_mueble = self.valida_continuar("A")
        if (status_mueble == 1):
            status_mueble = self.valida_continuar("A")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE CERRADO LADO A")

    def cerrar_solo_puerta_b(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("B")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 7):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta2_desplegar(False)
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 5):
            self.armar.puerta2_cerrar(False)
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 3):
            self.armar.poste2_cerrar(False)
            status_mueble = self.valida_continuar("B")
        if (status_mueble == 1):
            status_mueble = self.valida_continuar("B")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE CERRADO LADO B")

    def cerrar_mueble_completo(self):
        status_mueble = self.motores_posicion_mueble.consultar_status_mueble("C")
        if (status_mueble == 0):
            self.memoria.insertar_estados_finales_xml(3)
            self.error_fatal()
        if (status_mueble == 14):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta2_desplegar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 12):
            self.memoria.insertar_estados_finales_xml(2)
            self.armar.puerta2_desplegar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 11):
            self.armar.puerta1_desplegar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 10):
            self.armar.puerta1_desplegar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 9):
            self.armar.puerta2_cerrar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 8):
            self.armar.puerta2_cerrar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 7):
            self.armar.puerta1_cerrar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 6):
            self.armar.puerta1_cerrar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 5):
            self.armar.poste2_cerrar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 4):
            self.armar.poste2_cerrar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 3):
            self.armar.poste1_cerrar(False)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 2):
            self.armar.poste1_cerrar(True)
            status_mueble = self.valida_continuar("C")
        if (status_mueble == 1):
            status_mueble = self.valida_continuar("C")
            self.memoria.insertar_estados_finales_xml(3)
            print("MUEBLE COMPLETAMENTECERRADO")

    def valida_continuar(self,tipo):
        numero_status = 0
        if self.pruebas:
            validacion = True
            while validacion:
                numero_status = self.motores_posicion_mueble.consultar_status_mueble(tipo)
                continuar = raw_input("La posicion del diagrama es correcta s/n?")
                if continuar in ('s', 'S'):
                    self.memoria.insertar_proceso_xml(numero_status)
                    break
                else:
                    validacion = True
            return numero_status
        else:
            numero_status = self.motores_posicion_mueble.consultar_status_mueble(tipo)
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

    def sonido_inicial(self):
        print("EN FUNCIONAMIENTO")
        self.buzzer.on()
        sleep(2)
        self.buzzer.off()